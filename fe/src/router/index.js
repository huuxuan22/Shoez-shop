// src/router/index.js
import { createRouter, createWebHistory } from "vue-router";

// Views
import Home from "@/views/Home.vue";
import Login from "@/views/Login.vue";
import Register from "@/views/Register.vue";
import Contact from "@/views/Contact.vue";

// Templates
import AboutView from "@/templates/AboutView.vue";

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
    component: AboutView,
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
    component: () => import("@/views/Products.vue"),
    meta: {
      title: "Sản phẩm - Shoez Shop"
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

  // Check auth requirements (placeholder for future implementation)
  if (to.meta.requiresAuth) {
    const isAuthenticated = localStorage.getItem('token');
    if (!isAuthenticated) {
      next({ name: 'Login' });
      return;
    }
  }

  // Check guest requirements (redirect logged in users away from login/register)
  if (to.meta.requiresGuest) {
    const isAuthenticated = localStorage.getItem('token');
    if (isAuthenticated) {
      next({ name: 'Home' });
      return;
    }
  }

  next();
});

export default router;
