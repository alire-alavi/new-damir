<template>
  <div id="blog">
      <div class="allCatsForBlog" @click='closeMenu(),toggleBodyOverFlow()'>
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
      </div>
    <div id="blogWrapper">

        <div class="openCatsBtn">
            <button class='submit' @click.prevent='showCats=true,adjustation()'>دسته بندی موضوعات</button>
        </div>










      <consulate></consulate>

      <div class="blogPostWrapper">
        <single-post
          title="َشرینگ پک"
          descs="شیرینگ پک از کلمه انگلیسی شیرینک به معنای جمع شدن گرفته شده است . در این دستگاه سلفون و فیلم شیرینگ را با حرارت دادن جمع و بسته می‌کنند. به همین دلیل به این نوع عمل بسته بندی شیرینگ می‌گویند."
          img="/images/l30.jpg"
        ></single-post>
        <single-post
          title="َاب چسب"
          descs="شیرینگ پک از کلمه انگلیسی شیرینک به معنای جمع شدن گرفته شده است ."
          img="/images/abchasb.png"
        ></single-post>

        <single-post
          title="َاب چسب"
          descs="شیرینگ پک از کلمه انگلیسی شیرینک به معنای جمع شدن گرفته شده است ."
          img="/images/abchasb.png"
        ></single-post>
        <single-post
          title="َاب چسب"
          descs="شیرینگ پک از کلمه انگلیسی شیرینک به معنای جمع شدن گرفته شده است ."
          img="/images/abchasb.png"
        ></single-post>
        <single-post
          title="َاب چسب"
          descs="شیرینگ پک از کلمه انگلیسی شیرینک به معنای جمع شدن گرفته شده است ."
          img="/images/abchasb.png"
        ></single-post>
        <single-post
          title="َاب چسب"
          descs="شیرینگ پک از کلمه انگلیسی شیرینک به معنای جمع شدن گرفته شده است ."
          img="/images/abchasb.png"
        ></single-post>
        <single-post
          title="َاب چسب"
          descs="شیرینگ پک از کلمه انگلیسی شیرینک به معنای جمع شدن گرفته شده است ."
          img="/images/abchasb.png"
        ></single-post>
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
    animation:comIn 0.4s linear
}
.allBlogCatsWrapper{
    position: absolute;
    right:0;
    width:max-content;
    background: cornflowerblue;
    overflow: auto;
}
.allBlogCatsWrapper ul li{
    padding:12px;
    text-align:right
}
@keyframes comIn{
    from{
        left:100%
    }
    to{
        left:0
    }
}











#blog {
  margin-top: 60px;
  margin-bottom: 50px;
  width: 100%;
}
.blogPostWrapper {
  display: flex;
  width: 95%;
  flex-wrap: wrap;
  margin: auto;
  justify-content: center;
  max-width: 1500px;
}

.title p {
  color: rgb(236, 57, 68);
}
.openCatsBtn{
    display:flex;
    justify-content: center;
}
</style>