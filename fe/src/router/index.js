import { createRouter, createWebHistory } from "vue-router";
import { useAuthStore } from "@/stores/auth";
import Home from "@/views/Home.vue";
import Login from "@/views/Login.vue";
import Register from "@/views/Register.vue";
import Contact from "@/views/Contact.vue";
import AdminLogin from "@/views/AdminLogin.vue";
import About from "@/views/About.vue";
import ProductListLayout from "@/layouts/ProductListLayout.vue";

const routes = [
  {
    path: "/news/:id",
    name: "NewsDetail",
    component: () => import("@/views/NewsDetail.vue"),
    meta: {
      title: "Chi tiết bài báo - Shoez Shop"
    }
  },
  {
    path: "/policy/returns",
    name: "ReturnPolicy",
    component: () => import("@/views/ReturnPolicy.vue"),
    meta: {
      title: "Chính sách đổi trả - Shoez Shop"
    }
  },
  {
    path: "/guide/purchase",
    name: "PurchaseGuide",
    component: () => import("@/views/PurchaseGuide.vue"),
    meta: {
      title: "Hướng dẫn mua hàng - Shoez Shop"
    }
  },
  {
    path: "/policy/warranty",
    name: "Warranty",
    component: () => import("@/views/Warranty.vue"),
    meta: {
      title: "Bảo hành sản phẩm - Shoez Shop"
    }
  },
  {
    path: "/faq",
    name: "FAQ",
    component: () => import("@/views/FAQ.vue"),
    meta: {
      title: "FAQ - Hỏi đáp - Shoez Shop"
    }
  },
  {
    path: "/",
    name: "Home",
    component: Home,
    meta: {
      title: "Shoez Shop - Giày thể thao chính hãng"
    }
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
    meta: {
      title: "Đăng nhập - Shoez Shop",
      requiresGuest: true
    }
  },
  {
    path: "/register",
    name: "Register",
    component: Register,
    meta: {
      title: "Đăng ký - Shoez Shop",
      requiresGuest: true
    }
  },
  {
    path: "/about",
    name: "About",
    component: About,
    meta: {
      title: "Về chúng tôi - Shoez Shop"
    }
  },
  {
    path: "/contact",
    name: "Contact",
    component: Contact,
    meta: {
      title: "Liên hệ - Shoez Shop"
    }
  },
  // Future routes for e-commerce features
  {
    path: "/products",
    name: "Products",
    component: ProductListLayout,
    meta: {
      title: "Về chúng tôi - Shoez Shop"
    }
  },
  {
    path: "/products/:id",
    name: "ProductDetail",
    component: () => import("@/views/ProductDetail.vue"),
    meta: {
      title: "Chi tiết sản phẩm - Shoez Shop"
    }
  },
  {
    path: "/checkout",
    name: "Checkout",
    component: () => import("@/views/Checkout.vue"),
    meta: {
      title: "Thanh toán - Shoez Shop",
      requiresAuth: true  // 👈 Nên bảo vệ trang checkout
    }
  },
  {
    path: "/cart",
    name: "Cart",
    component: () => import("@/views/Cart.vue"),
    meta: {
      title: "Giỏ hàng - Shoez Shop",
      requiresAuth: true
    }
  },
  {
    path: "/profile",
    name: "Profile",
    component: () => import("@/views/Profile.vue"),
    meta: {
      title: "Hồ sơ - Shoez Shop",
      requiresAuth: true
    }
  },
  // Admin login route
  {
    path: "/admin/login",
    name: "AdminLogin",
    component: AdminLogin,
    meta: {
      title: "Admin Login - Shoez Shop",
      requiresGuest: true
    }
  },
  // Admin routes
  {
    path: "/admin",
    name: "AdminDashboard",
    component: () => import("@/views/admin/Dashboard.vue"),
    meta: {
      title: "Dashboard - Admin - Shoez Shop",
      requiresAuth: true,
      requiresAdmin: true
    }
  },
  {
    path: "/admin/products",
    name: "AdminProducts",
    component: () => import("@/views/admin/Products.vue"),
    meta: {
      title: "Quản lý sản phẩm - Admin - Shoez Shop",
      requiresAuth: true,
      requiresAdmin: true
    }
  },
  {
    path: "/admin/orders",
    name: "AdminOrders",
    component: () => import("@/views/admin/Orders.vue"),
    meta: {
      title: "Quản lý đơn hàng - Admin - Shoez Shop",
      requiresAuth: true,
      requiresAdmin: true
    }
  },
  {
    path: "/admin/customers",
    name: "AdminCustomers",
    component: () => import("@/views/admin/Dashboard.vue"), // Placeholder
    meta: {
      title: "Quản lý khách hàng - Admin - Shoez Shop",
      requiresAuth: true,
      requiresAdmin: true
    }
  },
  {
    path: "/admin/categories",
    name: "AdminCategories",
    component: () => import("@/views/admin/Dashboard.vue"), // Placeholder
    meta: {
      title: "Quản lý danh mục - Admin - Shoez Shop",
      requiresAuth: true,
      requiresAdmin: true
    }
  },
  {
    path: "/admin/brands",
    name: "AdminBrands",
    component: () => import("@/views/admin/Dashboard.vue"), // Placeholder
    meta: {
      title: "Quản lý thương hiệu - Admin - Shoez Shop",
      requiresAuth: true,
      requiresAdmin: true
    }
  },
  {
    path: "/admin/analytics",
    name: "AdminAnalytics",
    component: () => import("@/views/admin/Dashboard.vue"), // Placeholder
    meta: {
      title: "Thống kê - Admin - Shoez Shop",
      requiresAuth: true,
      requiresAdmin: true
    }
  },
  {
    path: "/admin/settings",
    name: "AdminSettings",
    component: () => import("@/views/admin/Dashboard.vue"), // Placeholder
    meta: {
      title: "Cài đặt - Admin - Shoez Shop",
      requiresAuth: true,
      requiresAdmin: true
    }
  },
  // Error pages
  {
    path: "/403",
    name: "Forbidden",
    component: () => import("@/views/Forbidden.vue"),
    meta: {
      title: "403 - Truy cập bị từ chối - Shoez Shop"
    }
  },
  {
    path: '/orders',
    name: 'Orders',
    component: () => import('@/views/Orders.vue'),
    meta: { requiresAuth: true }
  },
  {
    path: '/orders/:id',
    name: 'OrderDetail',
    component: () => import('@/views/OrderDetail.vue'),
    meta: {
      requiresAuth: true,
      title: 'Chi tiết đơn hàng - Shoez Shop'
    }
  },
  {
    path: "/:pathMatch(.*)*",
    name: "NotFound",
    component: () => import("@/views/NotFound.vue"),
    meta: {
      title: "Trang không tồn tại - Shoez Shop"
    }
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition;
    }
    return { top: 0 };
  }
});

// Navigation guards
// ============================================
// HƯỚNG DẪN: Cách phân loại trang trong router
// ============================================
// 1. TRANG PUBLIC (Không cần đăng nhập)
//    -> Không thêm meta gì, hoặc để rỗng
//    -> Ví dụ: Home, About, Contact, Products, ProductDetail
//
// 2. TRANG PROTECTED (Cần đăng nhập)
//    -> Thêm: meta: { requiresAuth: true }
//    -> Nếu chưa đăng nhập -> redirect về Login
//    -> Ví dụ: Cart, Profile, Orders, OrderDetail
//
// 3. TRANG GUEST-ONLY (Chỉ guest mới vào được)
//    -> Thêm: meta: { requiresGuest: true }
//    -> Nếu đã đăng nhập -> redirect về Home
//    -> Ví dụ: Login, Register, AdminLogin
//
// 4. TRANG ADMIN (Cần quyền admin)
//    -> Thêm: meta: { requiresAdmin: true }
//    -> Tự động check requiresAuth trước
//    -> Nếu không phải admin -> redirect về /403
//    -> Ví dụ: AdminDashboard, AdminProducts, AdminOrders
// ============================================

router.beforeEach((to, from, next) => {
  if (to.meta.title) {
    document.title = to.meta.title;
  }
  const authStore = useAuthStore();

  const isAuthenticated = authStore.isAuthenticated;
  const user = authStore.user;
  const isAdmin = authStore.isAdmin;

  // Check auth requirements - Cần đăng nhập
  if (to.meta.requiresAuth) {
    if (!isAuthenticated) {
      next({ name: 'Login' });
      return;
    }
  }

  // Check admin requirements - Cần quyền admin
  if (to.meta.requiresAdmin) {
    if (!isAuthenticated) {
      next({ name: 'AdminLogin' });
      return;
    }
    if (!isAdmin) {
      next({ name: 'Forbidden' });
      return;
    }
  }

  // Check guest requirements - Chỉ guest mới vào được (Login, Register)
  if (to.meta.requiresGuest) {
    if (isAuthenticated) {
      if (to.name === 'AdminLogin' && isAdmin) {
        next({ name: 'AdminDashboard' });
        return;
      }
      next({ name: 'Home' });
      return;
    }
  }

  next();
});

export default router;
