<template>
    <div id="app">
        <nav>
            <div class="div_nav_logo">
                <router-link :to="{name: 'Home'}"><img :src="logo"/></router-link>
            </div>
            <div class="div_nav_menu">
                <router-link :to="{name: 'Projects'}"><p>ПРОЕКТЫ</p></router-link>
                <template v-if="!logined">
                    <router-link :to="{name: 'Login'}"><p>ВХОД</p></router-link>
                    <router-link :to="{name: 'Registration'}"><p>РЕГИСТРАЦИЯ</p></router-link>
                </template>
                <template v-if="logined">
                    <p>Здравствуйте, {{ first_name }}!</p>
                    <p @click="handleLogoutClick" style="cursor: pointer">ВЫХОД</p>
                </template>
            </div>
        </nav>

        <main>
            <router-view/>
        </main>

        <footer>
            <div class="foot_logo">
                <img :src="logo"/>
            </div>

            <div class="foot_menu">
                <div class="foot_inf">
                    <p>Центральный офис</p>
                    <h5>+7 (495) 644-42-44</h5>
                </div>

                <div class="foot_inf">
                    <p>Общие вопросы</p>
                    <h5>info@coldy.ru</h5>
                </div>

                <div class="foot_inf">
                    <p>Реклама и PR</p>
                    <h5>pr@coldy.ru</h5>
                </div>
            </div>
        </footer>


    </div>
</template>
<script>
import logo from "./assets/logo.svg";
import {getUserName, logout} from "./api/auth";

export default {
    computed: {
        layout() {
            return this.$route.meta.layout || "default-layout"
        }
    },
    created() {
        getUserName()
            .then(first_name => {
                this.first_name = first_name
                this.logined = true
            })
    },
    data: function () {
        return {
            logo: logo,
            first_name: '',
            logined: false
        }
    },
    methods: {
        handleLogoutClick() {
            logout()
                .then(() => this.logined = false)
        }
    }
}
</script>

<style scoped>
main {
    max-width: 80%;
    margin-left: auto;
    margin-right: auto;
}

ul {
    list-style-type: none;
    margin: 0;
    padding: 0;
}

li {
    list-style-type: none;
    margin: 0;
    padding: 0;
}

a {
    text-decoration: none;
}


nav {
    max-width: 80%;
    margin-left: auto;
    margin-right: auto;
    padding-bottom: 20px;
    padding-top: 20px;
    display: flex;
}

nav ul img {
    width: 150px;
}

.div_nav_menu {
    display: flex;
    justify-content: space-between;
    position: absolute;
    right: 12%;
}

.div_nav_menu p {
    font-family: 'Raleway', sans-serif;
    margin-right: 15px;
    margin-left: 15px;
    font-size: 12px;
    color: #222222;
    font-weight: 600;
}

.div_nav_menu p:hover {
    color: #b68178;
}

.div_nav_menu p:active {
    color: #b68178;
}


footer {
    max-width: 80%;
    margin-left: auto;
    margin-right: auto;
    display: flex;
    margin-top: 300px;
    margin-bottom: 50px;
    justify-content: space-between;
}

.foot_inf {
    margin-right: 30px;
}

.foot_inf p {
    font-family: 'Raleway', sans-serif;
    font-weight: 500;
    color: #636363;
    font-size: 12px;
    line-height: 13px;
    margin-bottom: 20px;
    padding: 0px;
}

.foot_inf h5 {
    font-family: 'Raleway', sans-serif;
    font-weight: 500;
    color: #222222;
    font-size: 22px;
    line-height: 21px;
    padding: 0px;
    margin: 0px;
}

.foot_menu {
    display: flex;
}
</style>
