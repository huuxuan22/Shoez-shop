// src/router/index.js
import { createRouter, createWebHistory } from "vue-router";
import Login from "../views/Login.vue";
import Home from "./../views/Home.vue";
import Register from "@/views/Register.vue";
import Header from "@/views/Header.vue";
import Footer from "@/templates/Footer.vue";
import AboutView from "@/templates/AboutView.vue";
import Contact from "@/views/Contact.vue";

const routes = [
  {
    path: "/",
    name: "Login",
    component: Home
  },
  {
    path: "/header",
    name: "Header",
    component: Header
  },
  {
    path: "/about",
    name: "AboutView",
    component: AboutView
  },
  {
    path: "/contact",
    name: "Contact",
    component: Contact
  },
  {
    path: "/footer",
    name: "Footer",
    component: Footer
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
