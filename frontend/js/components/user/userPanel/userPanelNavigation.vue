<template>
    <div  id='userPanelNavigation' @click='toggleUserPanelNavigation(),toggleBodyOverFlow()'>
        <div id="userPanelNavigationWrapper" @click='prevent($event)'>
            <ul>
                <li @click="toggleUserPanelNavigation(),toggleBodyOverFlow()"> <router-link to="/userPanel">پروفایل</router-link> <img class='icon' src="/images/profile.png" alt=""></li>
                <li @click="toggleUserPanelNavigation(),toggleBodyOverFlow()"><router-link to="/userPanel/createProduct">اضافه کردن محصول برای فروش</router-link><img src="/images/sell.png" class='icon' alt=""></li>
                <li @click="toggleUserPanelNavigation(),toggleBodyOverFlow()"><router-link to="/userPanel/usersList">لیست کاربران</router-link><img src="/images/clipboard.png" class='icon' alt=""></li>
                <li @click="toggleUserPanelNavigation(),toggleBodyOverFlow()"><router-link to="/userPanel/createBlogPost">اضافه کردن پست بلاگ</router-link><img src="/images/sell.png" class='icon' alt=""></li>

            </ul>
        </div>
    </div>
</template>


<script>
    import {mapActions} from 'vuex'
    import {toggleBodyOverFlow} from "../mixIns/toggleBodyOverFlow"
	import {adjustElFromTop} from '../mixIns/adjustElFromTop.js'
    export default{
        name:"userPanelNavigation",
        mixins:[toggleBodyOverFlow,adjustElFromTop],
        methods:{
            ...mapActions([

                'toggleUserPanelNavigation',
                'swapUserPanelComponent'
            ]),
             prevent(e){
                e.stopPropagation();
                e.preventDefault();   
            }
        },
        mounted(){
            this.adjustFromTop(document.querySelector("#userPanelNavigationWrapper"))
		    this.toggleBodyOverFlow('hidden') 
        }
    }
</script>


<style scoped>
    ul{
        width:100%;
    }
    #userPanelNavigation{
        position:absolute;
        z-index:667;
        top:0;
        left:0;
        bottom:0;
        right:0;
        width:100%;
        height:100%;
        background: rgba(0,0,0,0.4);
    }
    #userPanelNavigationWrapper{
        background:rgb(74, 97, 143);
        position:absolute;
        right:0;
        top:0;
        bottom:0;
        max-width:80%;
        height:100vh
    }
    ul{
        display:flex;
        flex-direction:column;
        align-items: flex-end;
    }
    ul li{
        padding:10px;
        display:flex;
        align-items: center;
        justify-content: flex-end;
        text-align: right;
        width:100%;
        border-bottom:1px solid rgb(206, 187, 187)
    }
    ul li a{
        padding:10px;
        color:white;
    }
    .icon{
        width:30px;
        height:30px
    }

</style>