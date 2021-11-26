<template>
  <div class="main_signin">
    <form class="reg_form">
      <h1>Регистрация</h1>
      <div class="col">
        <input type="text" class="form-control form-control-lg" placeholder="Имя">
      </div>
      <div class="col">
        <input type="text" class="form-control form-control-lg" placeholder="Фамилия">
      </div>
      <div class="form-group">
        <input type="email" class="form-control form-control-lg" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Введите email">
      </div>
      <div class="form-group">
        <input type="password" class="form-control form-control-lg" id="exampleInputPassword1" placeholder="Введите пароль">
      </div>
      <div class="signing_but">
        <button type="button" class="btn btn-secondary btn-lg btn-block">Зарегистрироваться</button>
      </div>
    </form>
    <img :src="kaz_thesis"/>
  </div>
</template>

<script>
import kaz_thesis from "../assets/kaz_thesis.png"
export default {
  name: "Reg_page",
  data: function () {
    return {
      kaz_thesis: kaz_thesis
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
