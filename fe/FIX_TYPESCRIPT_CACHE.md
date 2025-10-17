# Hướng dẫn sửa lỗi TypeScript Cache

## Lỗi hiện tại:
```
File 'c:/duAnCSDLPQH/Shoez-shop/fe/src/components/ProductFilters.vue' not found.
```

## Nguyên nhân:
TypeScript/Volar đang cache đường dẫn cũ của ProductFilters.vue

## Giải pháp:

### Cách 1: Restart VSCode Language Server (Nhanh nhất)
1. Mở Command Palette (Ctrl+Shift+P hoặc Cmd+Shift+P)
2. Gõ: "TypeScript: Restart TS Server"
3. Hoặc: "Volar: Restart Vue Server"
4. Chọn và Enter

### Cách 2: Reload VSCode
1. Mở Command Palette (Ctrl+Shift+P)
2. Gõ: "Developer: Reload Window"
3. Enter

### Cách 3: Xóa cache và restart
1. Đóng VSCode
2. Xóa thư mục cache:
   - Windows: `C:\Users\[YourUser]\AppData\Roaming\Code\Cache`
   - hoặc xóa: `node_modules/.vite`
3. Mở lại VSCode

### Cách 4: Rebuild project
```bash
# Trong terminal
cd fe
npm run dev
```

## Xác nhận:
Sau khi làm một trong các cách trên, lỗi sẽ biến mất vì:
- ✅ File ProductFilters.vue đã tồn tại ở: `src/components/products/ProductFilters.vue`
- ✅ Import path đã đúng: `@/components/products/ProductFilters.vue`
- ✅ Không có file nào còn reference path cũ

## Kiểm tra lại:
Sau khi restart, mở file `src/views/Products.vue` và kiểm tra:
- Không còn lỗi đỏ ở dòng import
- Hover vào `ProductFilters` sẽ show đúng path
- Autocomplete sẽ hoạt động
