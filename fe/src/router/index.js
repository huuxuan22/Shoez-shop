// src/router/index.js
import { createRouter, createWebHistory } from "vue-router";
import Login from "../views/Login.vue";
import Home from "@/views/Home.vue";
import Register from "@/views/Register.vue";

const routes = [
  {
    path: "/",
    name: "Login",
    component: Login
  },
  {
    path: "/login",
    name: "Login",
    component: Login
  },
  {
    path: '/register',
    component: Register
  }
  
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
