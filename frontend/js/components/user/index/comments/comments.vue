<template>
    <div id="comments">
        <div id="commentsWrapper">
            <div class="marquee">
                <div class="singleTwinComment">
                    <div class="order1">
                        <div class="order1Wrapper">
                            <div class="name">
                                <p>عرفان</p>
                                <p class="categorie">شیرینگ مدل L30 | بسته بندی</p>
                            </div>
                            <div class="comment">
                                <p>لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ، و با استفاده از طراحان گرافیک است، چاپگرها و متون بلکه روزنامه و مجله در ستون و سطرآنچنان که </p>
                            </div>
                        </div>
                    </div>
                    <div class="order2">
                        <div class="order2Wrapper">
                            <div class="name">
                                <p>عرفان</p>
                                <p class="categorie">شیرینگ مدل L30 | بسته بندی</p>
                            </div>
                            <div class="comment">
                                <p>لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ، و با استفاده از طراحان گرافیک است، چاپگرها و متون بلکه روزنامه و مجله در ستون و سطرآنچنان که لازم است، و برای شرایط فعلی تکنولوژی مورد نیاز، و کاربردهای متنوع با هدف بهبود ابزارهای کاربردی می باشد، کتابهای </p>
                            </div>
                        </div>
                    </div>
                    <div class="order1">
                        <div class="order1Wrapper">
                            <div class="name">
                                <p>عرفان</p>
                                <p class="categorie">شیرینگ مدل L30 | بسته بندی</p>
                            </div>
                            <div class="comment">
                                <p>طراحان خلاقی، و فرهنگ پیشرو در زبان فارسی ایجاد کرد، در این صورت می توان امید داشت که تمام </p>
                            </div>
                        </div>
                    </div>
                    <div class="order2">
                        <div class="order2Wrapper">
                            <div class="name">
                                <p>عرفان</p>
                                <p class="categorie">شیرینگ مدل L30 | بسته بندی</p>
                            </div>
                            <div class="comment">
                                <p>لورم ایپسوم متن ساختگی با تولید سادگی نامفها و </p>
                            </div>
                        </div>
                    </div>
                    <div class="order1">
                        <div class="order1Wrapper">
                            <div class="name">
                                <p>عرفان</p>
                                <p class="categorie">شیرینگ مدل L30 | بسته بندی</p>
                            </div>
                            <div class="comment">
                                <p>لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت </p>
                            </div>
                        </div>
                    </div>
                    <div class="order2">
                        <div class="order2Wrapper">
                            <div class="name">
                                <p>عرفان</p>
                                <p class="categorie">شیرینگ مدل L30 | بسته بندی</p>
                            </div>
                            <div class="comment">
                                <p>لورم ایپسوم متن ساختگی با </p>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- <div class="singleTwinComment">
                    <div class="order1">
                        <div class="order1Wrapper">
                            <div class="name">
                                <p>عرفان</p>
                                <p class="categorie">شیرینگ مدل L30 | بسته بندی</p>
                            </div>
                            <div class="comment">
                                <p>لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت </p>
                            </div>
                        </div>
                    </div>
                    <div class="order2">
                        <div class="order2Wrapper">
                            <div class="name">
                                <p>عرفان</p>
                                <p class="categorie">شیرینگ مدل L30 | بسته بندی</p>
                            </div>
                            <div class="comment">
                                <p>لورم ایپسوم متن ساختگی با </p>
                            </div>
                        </div>
                    </div>
                </div> -->
                <!-- <div class="singleTwinComment">
                    <div class="order1">
                        <div class="order1Wrapper">
                            <div class="name">
                                <p>عرفان</p>
                                <p class="categorie">شیرینگ مدل L30 | بسته بندی</p>
                            </div>
                            <div class="comment">
                                <p>طراحان خلاقی، و فرهنگ پیشرو در زبان فارسی ایجاد کرد، در این صورت می توان امید داشت که تمام </p>
                            </div>
                        </div>
                    </div>
                    <div class="order2">
                        <div class="order2Wrapper">
                            <div class="name">
                                <p>عرفان</p>
                                <p class="categorie">شیرینگ مدل L30 | بسته بندی</p>
                            </div>
                            <div class="comment">
                                <p>لورم ایپسوم متن ساختگی با تولید سادگی نامفها و </p>
                            </div>
                        </div>
                    </div>
                </div> -->
            </div>
        </div>
    </div>

</template>


<style scoped>
#comments{
    background:#ffffff;
    margin-top:50px
}
    .marquee{
        display:flex;
    }
    .singleTwinComment{
        display:grid;
        grid-template-columns: repeat(auto-fit,minmax(max-content,250px));
        grid-template-rows: repeat(2,200px);
        grid-auto-flow: dense;        
    }
    .order1,.order2{
        /* max-width:300px; */
        /* width:max-content; */
        /* min-width: */
        margin:5px;
        border:1px solid rgb(175, 175, 175)
    }
    .order1Wrapper,.order2Wrapper{
        padding:5px
    }
    .categorie{
        font-size: 18px;
        margin-top: 5px;
        margin-bottom: 5px;
        color: rgb(9,111,211);
        font-weight: 800;
    }
</style>