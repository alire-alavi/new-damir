<template>
        <div id="customers">
            <div id="customersWrapper">
                <div class="title">
                    <p>مشتریان ما</p>
                </div>

                <div class="cusImgs">
                    <img alt="گلرنگ" title="گلرنگ" src="/images/ours1.png" >
                    <img alt="شرکت نفتت" title="شرکت نفتت" src="/images/ours2.png" >
                    <img alt="سایپا" title="سایپا" src="/images/ours3.png" >
                    <img alt="شیرین عسل" title="شیرین عسل" src="/images/ours4.png" >
                    <img alt="ایران خودرو" title="ایران خودرو" src="/images/ours5.png" >
                </div>
            </div>
        </div>

</template>

<style scoped>
#customers{
    background: #ffffff;
    margin-top:50px;
}
#customersWrapper{
    display:flex;
    flex-direction:column;
    justify-content: center;

}
.title p{
    text-align:center;
        font-size: 29px;
    font-weight: 800;
}
.cusImgs{
    display:flex;
    flex-wrap:wrap;
    justify-content: space-between;
}
.cusImgs img{
    filter:grayscale(1);
    width:200px;
    transition:all 0.4s
}
img:hover{
    filter:grayscale(0)
}
</style>