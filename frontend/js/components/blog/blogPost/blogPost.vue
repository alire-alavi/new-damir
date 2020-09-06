<template>
    <div id="singleBlogPostItem">
            <div class="signleBlogPostItemWrapper maxIs">
                <div class="postText">
                    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Velit quia aut, corporis ratione, distinctio magni ullam molestiae earum vitae illo aperiam. Consectetur amet numquam blanditiis quia inventore vitae a doloremque laboriosam non, modi ea sapiente illo ratione ut id ad dolores, possimus ab, atque enim? Aut eligendi veniam dignissimos quas earum, eum a modi esse asperiores dolor nobis, sint magnam dicta iste totam sapiente cum mollitia facilis expedita, aspernatur unde possimus illum! Tempora vero ea quas, odit, iste ab libero at delectus quia inventore error enim beatae excepturi. Fuga, atque. Iure distinctio sunt accusamus accusantium perferendis laborum voluptate, dolorem amet ex voluptas aperiam error aliquid alias, dignissimos placeat? Nemo quaerat voluptates aliquam nisi, fugiat distinctio reprehenderit minus aperiam quibusdam doloremque optio quisquam recusandae consectetur laudantium eos veritatis facilis suscipit praesentium nesciunt accusamus tenetur numquam enim totam assumenda? Possimus ipsam excepturi, dolores maxime iste qui aperiam sed aliquam. Consequuntur inventore repudiandae explicabo laboriosam ducimus optio sed tenetur nostrum ex voluptas dolores magni assumenda quibusdam a similique, illum at? Exercitationem excepturi, repellat aspernatur iste natus beatae. Suscipit, illum? Cumque est eaque eum aliquid necessitatibus. Ipsum nihil iure earum, quibusdam, culpa veniam, minus iusto blanditiis corrupti libero odit nisi eveniet velit. Veniam autem voluptatem nam magni tempore quo, distinctio soluta quasi illo maiores consequatur, labore minima animi commodi odio veritatis architecto perspiciatis deserunt qui, eveniet modi recusandae. Eaque deleniti dolorum temporibus! Quam magni, accusamus excepturi reprehenderit labore explicabo vero voluptatibus animi alias voluptate ut autem illo! Quo, explicabo aut! Et provident natus assumenda nam, non vel omnis maiores, minus quas nemo consectetur alias pariatur facere quos consequatur corrupti eveniet ullam sunt id tempora cumque quibusdam modi odio. Error, expedita. Asperiores et nulla, error nihil eaque, neque amet eum pariatur id, cupiditate iusto dolores veritatis! Unde aliquam quasi sapiente repudiandae repellat, eius rem facilis. Odit explicabo consequatur voluptas dignissimos. Aliquid maxime, debitis sed reiciendis architecto dicta aliquam eligendi quae officia? Ipsum odit non quas in quidem asperiores rem magni, delectus ullam minus nam fugit sed neque earum dolor, accusantium suscipit odio veniam doloremque quaerat, dolore doloribus quos cupiditate facere. Voluptate dicta, laboriosam voluptatem voluptatum hic, officiis voluptatibus tempore iusto quisquam ut consequuntur, dolorem eum doloribus libero itaque. Corporis temporibus libero ipsa soluta ducimus repellat. Quod repudiandae iste fugiat alias, ut beatae quidem esse veniam, laudantium totam ipsa illum, assumenda corporis nihil. Minus deleniti ea quasi rerum sit reprehenderit reiciendis nihil tenetur doloribus eveniet qui suscipit totam sint, cupiditate ut similique! Voluptatibus magnam provident vel tenetur ex consectetur dicta quis, excepturi, eos officiis vero voluptate dolor maiores et similique beatae voluptatem eveniet nesciunt quia repudiandae ea quod repellendus! Nisi culpa maiores labore debitis, animi asperiores architecto illo reprehenderit nostrum quisquam delectus maxime a distinctio reiciendis esse. Aperiam explicabo aspernatur hic voluptas minima? Repellat natus alias debitis ut et possimus odio eligendi placeat atque maxime officia fuga, sapiente quis tempore esse voluptatum cum enim at soluta eos exercitationem rem. Harum ipsam voluptatum esse, veritatis unde eaque adipisci perferendis nobis quos dicta, dignissimos alias odio. Illo, vel.</p>
                </div>



                <suggestin></suggestin>

                <comment-section></comment-section>
                



                <!-- <div class="comments">
                    <div class="commentsWrapper">
                        <div class="writeComment">
                            <textarea placeholder="نظر شما چیست؟" name="" id="" cols="30" rows="10"></textarea>
                            <button class='submit'>ثبت نظر</button>
                        </div>
                    </div>
                </div> -->



            </div>
        <consulate></consulate>
    </div>
</template>

<style scoped>
    .comments{
        margin-top:50px
    }
    .commentsWrapper{
        display:flex;
        flex-direction:column;
        align-items: center;
    }
    .writeComment{
        display:flex;
        flex-direction:column;
        align-items: center;
        width:100%
    }
    .writeComment button{
        width:max-content
    }
    textarea{
        margin-bottom:20px;
        width:80%;
        height:200px;
        resize: none;
        direction:rtl;
        font-size:14pt;
        font-family:'yekan';
        box-shadow: 0 5px 30px;
    }










    #singleBlogPostItem{
        display:flex;
        margin-top:50px;    
        justify-content: center;
    }
    .signleBlogPostItemWrapper{
        width: 90%;
    }
    
    
    p{
        text-align: justify;
    }
   
</style>

<script>
    import consulate from "../consulate/consulate.vue"
    import suggestin from "./suggestin.vue"
    import commentSection from "../../user/product/commentSection.vue"
    export default {
        components:{
            consulate,
            suggestin,
            commentSection
        }
    }
</script>