import { createRouter, createWebHistory } from "vue-router"

import HomeView from "../views/HomeView.vue"
import LoginView from "../views/LoginView.vue"
import RegisterView from "../views/RegisterView.vue"

import AdminDashboardView from "../views/AdminDashboardView.vue"
import AdminHomeView from "../views/AdminHomeView.vue"
import AdminStudentsView from "../views/AdminStudentsView.vue"
import AdminCompaniesView from "../views/AdminCompaniesView.vue"
import AdminPlacementDrivesView from "../views/AdminPlacementDrivesView.vue"
import AdminApplicationsView from "../views/AdminApplicationsView.vue"


const routes = [
    {path: "/", component: HomeView},
    {path: "/login", component: LoginView},
    {path: "/register", component: RegisterView},
    
    {path: "/admin_dashboard", component: AdminDashboardView, children: [
        {path: "", component: AdminHomeView},
        {path: "students", component: AdminStudentsView},
        {path: "companies", component: AdminCompaniesView,},
        {path: "placement_drives", component: AdminPlacementDrivesView},
        {path: "applications", component: AdminApplicationsView}
    ]}
]


const router = createRouter({
    history: createWebHistory(),
    routes
})


export default router