<template>
        <a href="pr_niceloft.html"><div class="projects">
          <h3>N'ICE LOFT</h3>
          <p>Москва</p>
          <p>Автомобильные проезд 4</p>
        </div></a>
</template>

<script>
export default {
  name: "Project_card",
  props: ['project_card'],
}
</script>

<style scoped>

.projects {
  height: 820px;
  background: url(/frontend/src/assets/pr_niceloft.png) rgba(0, 0, 0, 0.3);
  margin-top: 20px;
  padding: 0;
}

.projects h3 {
  font-family: 'Raleway', sans-serif;
  font-size: 90px;
  font-weight: 500;
  line-height: 1;
  color: #ffffff;
  margin: 0;
  padding-left: 20px;
  padding-top: 20px;
  margin-bottom: 10px;
}

.projects p {
  font-family: 'Raleway', sans-serif;
  font-size: 16px;
  font-weight: 500;
  color: #ffffff;
  padding-left: 20px;
  margin: 0;
}

#pr_kazakov {
  height: 820px;
  background: url(/frontend/src/assets/pr_kazakov.png) rgba(13%, 13%, 13%, 0.3);
  margin-top: 20px;
  padding: 0;
}

</style>

