"""
Socket.io Configuration
Giải thích: File này config Socket.io server để real-time communication
"""
import socketio

from utils.logger import logger

# Tạo Socket.IO server
# cors_allowed_origins: Cho phép frontend connect
# async_mode: Dùng async cho performance tốt hơn
sio = socketio.AsyncServer(
    cors_allowed_origins="*",  # Trong production nên chỉ định domain cụ thể
    async_mode='asgi',
    logger=False
)

socket_app = socketio.ASGIApp(sio)

# Namespace cho notifications
@sio.on('connect', namespace='/notifications')
async def connect(sid, environ):
    """
    Giải thích: Khi client connect vào namespace /notifications
    - sid: Session ID của client
    - Trả về 'connected' để client biết đã kết nối thành công
    """
    await sio.emit('status', {'status': 'connected'}, room=sid)
    return True

@sio.on('disconnect', namespace='/notifications')
async def disconnect(sid):
    """
    Giải thích: Khi client disconnect
    """
    logger.info(f'Client disconnected: {sid}')

@sio.on('join_user_room', namespace='/notifications')
async def join_user_room(sid, data):
    """
    Giải thích: User join vào room của mình
    - Mỗi user có room riêng theo user_id
    - Khi có notification, emit vào room đó
    """
    user_id = data.get('user_id')
    if not user_id:
        logger.warning(f'join_user_room - user_id is missing in data: {data}')
        return {'status': 'error', 'message': 'user_id is required'}
    
    # Normalize user_id to string
    normalized_user_id = str(user_id).strip()
    room = f'user_{normalized_user_id}'
    await sio.enter_room(sid, room, namespace='/notifications')
    logger.info(f'User {normalized_user_id} (sid: {sid}) joined room {room}')
    return {'status': 'joined', 'room': room}

@sio.on('join_room', namespace='/notifications')
async def join_room(sid, data):
    """
    Giải thích: Admin join vào admin room
    - Admin join room 'admin' để nhận notifications về đơn hàng mới
    """
    room = data.get('room', 'admin')
    await sio.enter_room(sid, room, namespace='/notifications')
    logger.info(f'Client {sid} joined room {room}')
    return {'status': 'joined', 'room': room}

def get_sio():
    return sio

