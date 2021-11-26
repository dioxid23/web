<template>
    <section class="projects_page">
      <div v-for="item in project_card" class="projects-item">
        <Project_card :project_card="item"></Project_card>
      </div>
    </section>
</template>

<script>
import Project_card from "../components/Project_card";

export default {
  name: "Projects",
  components: {Project_card},
  data() {
    return {
      project_card: [
        {
          id: 1,
          name: 'NICE LOFT',
          city: 'Москва',
          address: 'Автомобильные проезд 4'
        },
        {
          id: 2,
          name: 'KAZAKOV GRAND LOFT',
          city: 'Москва',
          address: 'улица Казакова 7'
        }
      ]
    }
  },
}
</script>

<style scoped>
.projects_page {
  display: flex;
  justify-content: space-between;
}

</style>
