<template>
    <div id="userPanel" class='mainItemForUserPanel shouldCollapse maxIs'>
        <div id="userPanelWrapper">
            <div id="userPanelNavigationOpenBtn">
                <button class='submit' @click='toggleUserPanelNavigation()'>منوی کاربری</button>
            </div>
            
            
            <user-panel-navigation v-if='shoudIShow'></user-panel-navigation>

                <transition name="router" mode="out-in">
                    <keep-alive><router-view  /></keep-alive>
                
                </transition>
            
        </div>
        
    </div>    
</template>

<script>
    import {mapActions} from 'vuex'
    import userPanelNavigation from "./userPanelNavigation.vue"
    import {toggleBodyOverFlow} from "../mixIns/toggleBodyOverFlow.js"
	import {adjustElFromTop} from '../mixIns/adjustElFromTop.js'
    export default{
        name:"userPanel",
        mixins:[toggleBodyOverFlow,adjustElFromTop],
        components:{
            userPanelNavigation,
            // createProduct,
            // profile
        },
        methods:{
            ...mapActions([
                'toggleUserPanelNavigation'
            ])
        },
        computed:{
            shoudIShow(){
                return this.$store.state.isShowUserPanelNavigation
            }, 
        }
    }
</script>


<style scoped>
    #userPanel{
        margin-top:20px;

    }
    #userPanelWrapper{
        display:flex;
        width:100%;
        align-content: center;
        flex-direction:column;
    }
    #userPanelNavigationOpenBtn{
        display:flex;
        flex-direction:column;
        align-items: center;
    }
    .submit{
        max-width:max-content
    }
    .userPanelComp{
        background: white;
    }
    .router-enter-active{
        opacity:0;
        animation:expnad 0.5s linear forwards;
    }
    .router-leave-active{
        opacity:1;
        animation:expnadOff 0.5s linear forwards;
    }
    @keyframes expnad {
        from{
            opacity: 0
        }
        to{
            opacity: 1
        }
    }
    @keyframes expnadOff {
        from{
            opacity: 1
        }
        to{
            opacity: 0
        }
    }


</style>