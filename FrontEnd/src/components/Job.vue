<template>
    <card type="secondary" shadow class="border-0 mb-4 mt-4">
        <div class=" border-bottom pb-2">
          {{job.company}} - {{job.title}}
          <br>
          <small> {{job.location}} </small>
        </div> 
        <div class="mt-3">
          {{job.description}}
        </div>
        <div class="text-right">
          <base-button type="success" class="mt-2">Apply</base-button>
        </div>
    </card>
</template>

<script>
export default {
    name: 'Job',
    props: {
        job: {
      type: Object,
    },
    data(){
        return{
            activeColor: 'lightgreen',
        }
    }
    }
}
</script>

<style scoped>

</style>