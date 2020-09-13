<template>
  <div id="blog">
      <!-- <div class="allCatsForBlog" @click='closeMenu(),toggleBodyOverFlow()'>
          <div class="allBlogCatsWrapper" @click='preventDef($event)'>
              <ul>
                  <li><a href="#">شرینگ پک</a></li>
                  <li><a href="#">درب بند</a></li>
                  <li><a href="#">خط تولید پنیر پیتزا</a></li>
                  <li><a href="#">شرینگ پک</a></li>
                  <li><a href="#">شرینگ پک</a></li>
                  <li><a href="#">شرینگ پک</a></li>
                  <li><a href="#">شرینگ پک</a></li>
                  <li><a href="#">شرینگ پک</a></li>
                  <li><a href="#">شرینگ پک</a></li>
                  <li><a href="#">شرینگ پک</a></li>
                  <li><a href="#">شرینگ پک</a></li>
                  <li><a href="#">شرینگ پک</a></li>
                  <li><a href="#">شرینگ پک</a></li>
                  <li><a href="#">شرینگ پک</a></li>
                  <li><a href="#">شرینگ پک</a></li>
                  <li><a href="#">شرینگ پک</a></li>
                  <li><a href="#">شرینگ پک</a></li>
                  <li><a href="#">شرینگ پک</a></li>
                  <li><a href="#">شرینگ پک</a></li>
                  <li><a href="#">شرینگ پک</a></li>
                  <li><a href="#">شرینگ پک</a></li>
                  <li><a href="#">شرینگ پک</a></li>
                  <li><a href="#">شرینگ پک</a></li>
                  <li><a href="#">شرینگ پک</a></li>
                  <li><a href="#">شرینگ پک</a></li>
                  <li><a href="#">شرینگ پک</a></li>
                  <li><a href="#">شرینگ پک</a></li>
                  <li><a href="#">شرینگ پک</a></li>
                  <li><a href="#">شرینگ پک</a></li>
                  <li><a href="#">شرینگ پک</a></li>
              </ul>
          </div>
      </div> -->
    <div id="blogWrapper">

        <!-- <div class="openCatsBtn">
            <button class='submit' @click.prevent='showCats=true,adjustation()'>دسته بندی موضوعات</button>
        </div> -->










      <!-- <consulate></consulate> -->

      <div class="blogPostWrapper">
        <div v-for="(p,i) in JSON.parse(posts)" :key="i">
          <a :href="getSlugn(p)">
              <single-post
              :title="p.title"
              :descs="p.short_description"
              :author="p.author"
              :img="p.thumbnail"
            ></single-post> 
          </a>          
          
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import singlePost from "./singlePost.vue";
import consulate from "../consulate/consulate.vue";
import {adjustElFromTop} from '../../user/mixIns/adjustElFromTop.js'
import {toggleBodyOverFlow} from '../../user/mixIns/toggleBodyOverFlow.js'
export default {
  components: {
    singlePost,
    consulate,
  },
  props:['posts'],
  created(){
    console.log("posts",JSON.parse(this.posts))
  },
  mixins:[toggleBodyOverFlow,adjustElFromTop],
  data(){
      return{
          showCats:false
      }
  },
  methods: {
    startValidation(type, e) {
      const el = e.target;
      const parentNode = e.target.parentElement;

      const error = parentNode.nextElementSibling;
      if (el.id == "userPassword" && el.value.length < 8) {
        error.style.visibility = "visible";
        el.classList.remove("correct");
        el.classList.add("wrong");
        return;
      }
      const res = this.validateUserInput(type, e);
      if (res) {
        error.style.visibility = "hidden";
        return;
      }
      error.style.visibility = "visible";
    },
    preventDef(e){
      e.stopPropagation()
      e.preventDefault()
    },
    adjustation(){
        this.showCats=true
        const el=document.querySelector('.allBlogCatsWrapper')
        const all=document.querySelector(".allCatsForBlog")
        all.style.display="block"
        console.log("docdoc",el)
        this.toggleBodyOverFlow("hidden")
        this.adjustFromTop(el)
        
    },
    closeMenu(){
        const all=document.querySelector(".allCatsForBlog")
        all.style.display="none"
        this.toggleBodyOverFlow()
    },
    getSlugn(p){
      return `/blog/post/${p.slug}`
    }
  },
  
};
</script>


<style scoped>
.allCatsForBlog{
    position:absolute;
    z-index:669;
    width:100%;
    height:100%;
    top:0;
    background: rgba(0,0,0,0.8);
    display:none;
}
.allBlogCatsWrapper{
    position: absolute;
    right:0;
    width:max-content;
    background: #ffffff;
    overflow: auto;
}
.allBlogCatsWrapper ul li{
    padding:12px;
    text-align:right
}




#blog {
  margin-top: 60px;
  margin-bottom: 50px;
  width: 100%;
}
.blogPostWrapper {
  display: flex;
  max-width:1200px;
  flex-wrap: wrap;
  margin: auto;
  justify-content: center;
}

.title p {
  color: rgb(236, 57, 68);
}
.openCatsBtn{
    display:flex;
    justify-content: center;
}
.allBlogCatsWrapper{
  transition:all 0.5;
  animation:comeRight 0.5s
}
@keyframes comeRight{
  from{
    right:-100%
  }
  to{
    right:0
  }
}
</style>