// src/router/index.js
import { createRouter, createWebHistory } from "vue-router";

// Views
import Home from "@/views/Home.vue";
import Login from "@/views/Login.vue";
import Register from "@/views/Register.vue";
import Contact from "@/views/Contact.vue";
import AdminLogin from "@/views/AdminLogin.vue";

// Templates
import AboutView from "@/templates/AboutTemplate.vue";
import About from "@/views/About.vue";
import ProductListLayout from "@/layouts/ProductListLayout.vue";

const routes = [
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
      title: "Chi tiết sản phẩm - Shoez Shop"
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
    // Always scroll to top when navigating to a new route
    if (savedPosition) {
      return savedPosition;
    }
    return { top: 0 };
  }
});

// Navigation guards
router.beforeEach((to, from, next) => {
  // Set page title
  if (to.meta.title) {
    document.title = to.meta.title;
  }

  const isAuthenticated = localStorage.getItem('token');
  const user = localStorage.getItem('user') ? JSON.parse(localStorage.getItem('user')) : null;
  const isAdmin = user?.role?.toLowerCase() === 'admin' || user?.role?.toLowerCase() === 'administrator';

  // Check auth requirements
  if (to.meta.requiresAuth) {
    if (!isAuthenticated) {
      next({ name: 'Login' });
      return;
    }
  }

  // Check admin requirements
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

  // Check guest requirements (redirect logged in users away from login/register)
  if (to.meta.requiresGuest) {
    if (isAuthenticated) {
      // If trying to access admin login but already logged in as admin
      if (to.name === 'AdminLogin' && isAdmin) {
        next({ name: 'AdminDashboard' });
        return;
      }
      // Regular user trying to access login
      next({ name: 'Home' });
      return;
    }
  }

  next();
});

export default router;
