<template>
    <div id="products" class='shouldCollapse maxIs'>
        <div id="productsWrapper">


            <div class="singleProduct" v-for='p in JSON.parse(this.products)' :key='p.slug'>
                <div class="img">
                    <!-- <img src="/images/1.jpg" alt=""> -->
                    <zoom-on-hover :img-normal="getImage(p.product_image)"></zoom-on-hover>
                </div>
                <div class="title">
                    <a :href="gethref(p.slug)"><p>{{p.title}}</p></a>
                </div>
                <div class="price">
                    <p>{{p.price}} تومان</p>
                    <p>کشور ساخت:{{p.made_in}}</p>
                </div>
                <div class="contactUs">
                    <button class="stelam" @click.prevent='showConsulate($event)'>استعلام قیمت</button>
                </div>
                <consulate :productName="p.title"></consulate>
            </div>




            
            
        </div>

    </div>
</template>

<style scoped>
#products{
    margin-top:50px
}
#productsWrapper{
    display:flex;
    flex-wrap: wrap;
    justify-content: center;
}
.singleProduct{
    width:23%;
    margin:10px;
    width:300px
}
img{
    height:300px;
    width:300px;
    
}
.title{
    height:100px
}
.contactUs{
    display:flex;
    justify-content: center;
    margin-top:5px;
}
img.normal{
    width: 100%;
    height: 300px !important;
}

</style>

<script>
    import {mapActions} from 'vuex'
    import consulate from "./consulate.vue"
    import filtering from "./filtering.vue"
     import {adjustElFromTop} from "../../user/mixIns/adjustElFromTop.js"
     import {toggleBodyOverFlow} from "../../user/mixIns/toggleBodyOverFlow.js"
    export default{
        props:['products',"pagination"],
        mounted(){
            console.log(JSON.parse(this.products),this.pagination)
            const allImages=document.querySelectorAll(".normal")
            allImages.forEach(img=>{
                console.log(img)
                img.style.width='100%'
                img.style.height="300px"
                const zoom=img.nextElementSibling
                zoom.style.width="200%"
                zoom.style.width="200%"
            })
        },
        components:{
            consulate,
            filtering
        },
        mixins:[adjustElFromTop],
        data(){
            return{
                descs:'محصول ساخت چین قدرت تولید صدا تا 1200 دسیبل دارای باتری 36 ولت فلان لان فلان فلان فلان فلان فلان فلان فلان فلان  فلان فلان فلان فلان فلان فلان فلان فلان  فلان فلان فلان فلان فلان فلان فلان فلان  فلان فلان فلان فلان فلان فلان فلان فلان  فلان فلان فلان فلان فلان فلان فلان فلان  فلان فلان فلان فلان فلان فلان فلان فلان  فلان فلان فلان فلان فلان فلان فلان فلان  فلان فلان فلان فلان فلان فلان فلان فلان  فلان فلان فلان فلان فلان فلان فلان فلان  فلان فلان فلان فلان فلان فلان فلان فلان  فلان فلان فلان فلان فلان فلان فلان فلان  فلان فلان فلان فلان فلان فلان فلان فلان  فلان فلان فلان فلان فلان فلان فلان فلان  فلان فلان فلان فلان فلان فلان فلان فلان  فلان فلان فلان فلان فلان فلان فلان فلان  فلان فلان فلان فلان فلان فلان فلان فلان  فلان فلان فلان فلان فلان فلان فلان فلان  فلان فلان فلان فلان فلان فلان فلان فلان  فلان فلان فلان فلان فلان فلان فلان فلان  فلان فلان فلان فلان فلان فلان فلان فلان  فلان فلان فلان فلان فلان فلان فلان فلان  فلان فلان فلان فلان فلان فلان فلان فلان فلان فلان فلان فلان فلان فلان فلان لان فلان فلان الن'
            }
        },
        methods:{
            ...mapActions([
               'toggleFiltering',
               'toggleConsulate'
            ]),
            getDescs(){
                return this.descs.length>100 ? this.descs.substring(0,200)+'...' : this.descs
            },
            adjustConsulateTop(){
                const consulate=document.querySelector("#consulateWrapper")
                consulate.style.top=window.scrollY+100+"px"
                document.body.style.overflow='hidden'
                const done=document.querySelector("#doneMessage")
                done.style.display='none'
            },
            shoudShow(){
                return this.$store.state.isShowFiltering
            },
            showConsulate(e){
                const el=e.target;
                const parent=el.closest(".singleProduct")
                const consulate=parent.querySelector(".consulate")
                const wrap=consulate.querySelector(".consulateWrapper")
                consulate.style.display="flex"
                this.adjustFromTop(wrap,false,true)
                this.toggleBodyOverFlow("hidden")
                
            },
            getImage(img){
                if(img==null){
                    return '/images/ours1.png'
                }
                return img
            },
            gethref(slug){
                return `/products/${slug}`
            }
        }
    }
</script>