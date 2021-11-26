<template>
  <div>
    <div id="img_hero" class="div_hero_img">
      <img :src="hero_img"/>
    </div>

    <div class="div_hero">
      <h3>KAZAKOV GRAND LOFT</h3>
      <h6>MADE IN 2020</h6>
      <p>Kazakov Grand Loft — новый комплекс апартаментов в исторической части Москвы.
        Продуманное до мелочей содержание и безукоризненная форма.</p>
    </div>

    <div class="div_make">
      <h4>WE MAKE NEW LIVING</h4>
      <p>Мы создаем проекты, которые меняют повседневную жизнь, собирают вместе единомышленников
        и новое поколение жителей мегаполиса.</p>
      <p>Проекты COLDY предвосхищают ваши интересы и желания.</p>
    </div>

    <div id="img_coldy">
      <img :src="block_coldy"/>
    </div>
    <div class="div_coldy">
      <h4>COLDY</h4>
      <p>Наша команда — сообщество людей, устремленных в будущее, которые бережно относятся
        к архитектурным традициям и ценят индивидуальность: каждый сотрудник и проект компании уникальны.</p>
      <p>Coldy — наш ежедневный драйв, который заряжает на новые свершения.</p>
      <p>17 лет мы задаём новые стандарты качества, ежедневно открывая новые возможности и сохраняя
        память города.</p>

    </div>


    <div class="div_command">
      <h4>КОМАНДА</h4>
      <p>Хочешь сделать что-то идеальным — начни с себя. Так считаем мы, принимая в команду амбициозных людей,
        для которых работа — это драйв и творчество, выход за рамки стереотипов.</p>
      <p>Мы радуемся новым вызовам так же сильно, как и новым победам.</p>
      <p>Мы гордимся своим уровнем, но всегда готовы расти дальше. И для этого у нас есть все условия.</p>
    </div>
    <div class="img_command">
      <img :src="comand1"/>
      <img :src="comand2"/>
    </div>

    <div class="progr_loyalty">
      <h4>ПРОГРАММА ЛОЯЛЬНОСТИ</h4>
      <p>Мы создаем проекты, которые меняют повседневную жизнь, собирают вместе единомышленников и новое
        поколение жителей мегаполиса. Проекты MADE IN COLDY предвосхищают ваши интересы и желания.</p>
    </div>
    <div id="img_loyalty">
      <img :src="loyalty"/>
    </div>
  </div>

</template>

<script>
import hero_img from "../assets/hero_img.png"
import block_coldy from "../assets/block_coldy.jpg"
import comand1 from "../assets/comand1.png"
import comand2 from "../assets/comand2.png"
import loyalty from "../assets/loyalty.png"

export default {
  name: "Home_page",
  data: function () {
    return {
      hero_img: hero_img,
      block_coldy: block_coldy,
      comand1: comand1,
      comand2: comand2,
      loyalty: loyalty
    }
  }

}
</script>

<style scoped>
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

.div_hero {
  max-width: 40%;
  margin-bottom: 350px;
  margin-top: 200px;
}

.div_hero h3 {
  font-family: 'Raleway', sans-serif;
  font-size: 90px;
  font-weight: 500;
  line-height: 1;
  color: #636363;
  margin: 0;
  padding: 0;
}

.div_hero h6 {
  font-family: 'Raleway', sans-serif;
  font-weight: 500;
  color: #b68178;
  font-size: 11px;
  margin-top: 10px;
  margin-bottom: 30px;
  padding: 0;
}

.div_hero p {
  font-family: 'Raleway', sans-serif;
  font-weight: 500;
  color: #636363;
  font-size: 16px;
  max-width: 60%;
  margin-left: auto;
}

#img_hero {
  float: right;
  position: relative;
  top: -140px;
  left: -50px;
}

.div_hero_img img {
  width: 650px;
}

.div_make {
  max-width: 35%;
  margin-left: auto;
  margin-right: auto;
  margin-top: 160px;
}

.div_make h4 {
  font-family: 'Raleway', sans-serif;
  font-weight: 400;
  color: #636363;
  font-size: 80px;
  line-height: 1;
  margin-bottom: 50px;
  padding: 0;
}

.div_make p {
  font-family: 'Raleway', sans-serif;
  font-weight: 500;
  color: #636363;
  font-size: 16px;
  max-width: 60%;
  line-height: 21px;
  margin-left: auto;
  margin-bottom: 15px;
}

.div_coldy {
  max-width: 35%;
  margin-left: auto;
  margin-right: auto;
  margin-top: 160px;
}

.div_coldy h4 {
  font-family: 'Raleway', sans-serif;
  font-weight: 400;
  color: #636363;
  font-size: 80px;
  line-height: 1;
  margin-bottom: 50px;
  padding: 0;
}

.div_coldy p {
  font-family: 'Raleway', sans-serif;
  font-weight: 500;
  color: #636363;
  font-size: 16px;
  max-width: 60%;
  line-height: 21px;
  margin-left: auto;
  margin-bottom: 15px;
}

.div_command {
  max-width: 35%;
  margin-left: auto;
  margin-right: auto;
  margin-top: 550px;
}

.div_command h4 {
  font-family: 'Raleway', sans-serif;
  font-weight: 400;
  color: #636363;
  font-size: 80px;
  line-height: 1;
  margin-bottom: 50px;
  padding: 0;
}

.div_command p {
  font-family: 'Raleway', sans-serif;
  font-weight: 500;
  color: #636363;
  font-size: 16px;
  max-width: 60%;
  line-height: 21px;
  margin-left: auto;
  margin-bottom: 15px;
}

.img_command img {
  max-width: 45%;
}

.progr_loyalty {
  max-width: 35%;
  margin-left: auto;
  margin-right: auto;
  margin-top: 160px;
}

.progr_loyalty h4 {
  font-family: 'Raleway', sans-serif;
  font-weight: 400;
  color: #636363;
  font-size: 80px;
  line-height: 1;
  margin-bottom: 50px;
  padding: 0;
}

.progr_loyalty p {
  font-family: 'Raleway', sans-serif;
  font-weight: 500;
  color: #636363;
  font-size: 16px;
  max-width: 60%;
  line-height: 21px;
  margin-left: auto;
  margin-bottom: 15px;
}

#img_coldy {
  float: left;
  position: relative;
  top: 290px;
}
</style>

