<template>
    <div class="main_signin">

        <form class="signin_form">
            <h1>Вход</h1>
            <div class="form-group">
                <input type="email" class="form-control form-control-lg" id="exampleInputEmail1"
                       aria-describedby="emailHelp" placeholder="Введите email" v-model="userData.username">
            </div>
            <div class="form-group">
                <input type="password" class="form-control form-control-lg" id="exampleInputPassword1"
                       placeholder="Введите пароль" v-model="userData.password">
            </div>
            <div class="signing_but">
                <button type="button" class="btn btn-secondary btn-lg btn-block" @click="handleLoginClick">Войти</button>
            </div>
        </form>

        <img :src="signin"/>
    </div>
</template>

<script>
import signin from "../assets/signin.png"
import {login} from "../api/auth";

export default {
    name: "Login_page",
    data: function () {
        return {
            signin: signin,
            userData: {
                username: '',
                password: ''
            }
        }
    },
    methods: {
        handleLoginClick(){
            login(this.userData)
                .then(() => this.$router.push('/'))
        }
    }
}
</script>

<style scoped>
.main_signin {
    margin-left: auto;
    margin-right: auto;
    display: flex;
    padding: 50px;
    background: #f9f9f9;
}

.main_signin img {
    max-width: 50%;
}

.signin_form {
    max-width: 50%;
    margin-right: auto;
    margin-top: 150px;
}

.form-group {
    margin-bottom: 10px;
}

.signing_but {
    margin-top: 20px;
}

.signin_form h1 {
    font-family: 'Raleway', sans-serif;
    font-size: 40px;
    font-weight: 500;
    color: #636363;
    margin-bottom: 25px;
}

</style>
