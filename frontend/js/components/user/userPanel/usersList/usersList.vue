<template>
    <div id="usersList" >
        <users-filter></users-filter>
        <user-list-table></user-list-table>
        
    </div>
</template>

<style scoped>
    #usersList{
        display:flex;
        flex-direction:column;
        align-items: center;
        margin:auto
    }

    
    
</style>

<script>
import usersFilter from "./usersFilter.vue"
    import userListTable from './usersListTable.vue'
    export default{
        components:{
            userListTable,
            usersFilter
        }
    }

</script>