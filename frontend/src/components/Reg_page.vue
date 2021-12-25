<template>
    <div class="main_signin">
        <form class="reg_form">
            <h1>Регистрация</h1>
            <div class="col">
                <input type="text" class="form-control form-control-lg" placeholder="Имя" v-model="userData.first_name">
            </div>
            <div class="col">
                <input type="text" class="form-control form-control-lg" placeholder="Фамилия"
                       v-model="userData.last_name">
            </div>
            <div class="form-group">
                <input type="email" class="form-control form-control-lg" id="exampleInputEmail1"
                       aria-describedby="emailHelp" placeholder="Введите email" v-model="userData.email">
            </div>
            <div class="form-group">
                <input type="password" class="form-control form-control-lg" id="exampleInputPassword1"
                       placeholder="Введите пароль" v-model="userData.password">
            </div>
            <div class="signing_but">
                <button type="button" class="btn btn-secondary btn-lg btn-block" @click="handleRegisterClick">
                    Зарегистрироваться
                </button>
            </div>
        </form>
        <img :src="kaz_thesis"/>
    </div>
</template>

<script>
import kaz_thesis from "../assets/kaz_thesis.png"
import {register} from "../api/auth";

export default {
    name: "Reg_page",
    data: function () {
        return {
            kaz_thesis: kaz_thesis,
            userData: {
                first_name: '',
                last_name: '',
                email: '',
                password: ''
            }
        }
    },
    methods: {
        handleRegisterClick() {
            register(this.userData)
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

.reg_form {
    max-width: 50%;
    margin-right: auto;
    margin-top: 150px;
}

.reg_form h1 {
    font-family: 'Raleway', sans-serif;
    font-size: 40px;
    font-weight: 500;
    color: #636363;
}

.col {
    margin-bottom: 10px;
}
</style>
