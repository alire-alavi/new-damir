<template>
    <div class="other">
                    <div class="singleOther">
                        <div class="otherWrapper">
                            
                            <div class="otherImg">
                                <img src="/images/2.jpg" alt="">
                            </div>
                            <div class="otherTitle">
                                <a href="#">شرینگ پک</a>
                            </div>
                            <div class="otherModel">
                                 <button><svg class="icon-svg iconSvg-style" width="24" height="24" viewBox="0 0 24 24">
                                    <path d="M17.016 3c1.078 0 1.969 0.938 1.969 2.016v15.984l-6.984-3-6.984 3v-15.984c0-1.078 0.891-2.016 1.969-2.016h10.031z"></path>
                                </svg></button>
                                <a href="#">مدل شرینگ پک L30</a>
                            </div>
                        </div>
                    </div>
                    <div class="singleOther">
                        <div class="otherWrapper">
                            
                            <div class="otherImg">
                                <img src="/images/2.jpg" alt="">
                            </div>
                            <div class="otherTitle">
                                <a href="#">شرینگ پک</a>
                            </div>
                            <div class="otherModel">
                                 <button><svg class="icon-svg iconSvg-style" width="24" height="24" viewBox="0 0 24 24">
                                    <path d="M17.016 3c1.078 0 1.969 0.938 1.969 2.016v15.984l-6.984-3-6.984 3v-15.984c0-1.078 0.891-2.016 1.969-2.016h10.031z"></path>
                                </svg></button>
                                <a href="#">مدل شرینگ پک L30</a>
                            </div>
                        </div>
                    </div>
                    <div class="singleOther">
                        <div class="otherWrapper">
                            
                            <div class="otherImg">
                                <img src="/images/2.jpg" alt="">
                            </div>
                            <div class="otherTitle">
                                <a href="#">شرینگ پک</a>
                            </div>
                            <div class="otherModel">
                                 <button><svg class="icon-svg iconSvg-style" width="24" height="24" viewBox="0 0 24 24">
                                    <path d="M17.016 3c1.078 0 1.969 0.938 1.969 2.016v15.984l-6.984-3-6.984 3v-15.984c0-1.078 0.891-2.016 1.969-2.016h10.031z"></path>
                                </svg></button>
                                <a href="#">مدل شرینگ پک L30</a>
                            </div>
                        </div>
                    </div>
                    <div class="singleOther">
                        <div class="otherWrapper">
                            
                            <div class="otherImg">
                                <img src="/images/2.jpg" alt="">
                            </div>
                            <div class="otherTitle">
                                <a href="#">شرینگ پک</a>
                            </div>
                            <div class="otherModel">
                                 
                                 <button><svg class="icon-svg iconSvg-style" width="24" height="24" viewBox="0 0 24 24">
                                    <path d="M17.016 3c1.078 0 1.969 0.938 1.969 2.016v15.984l-6.984-3-6.984 3v-15.984c0-1.078 0.891-2.016 1.969-2.016h10.031z"></path>
                                </svg></button>
                                <a href="#">مدل شرینگ پک L30</a>
                            </div>
                        </div>
                    </div>
                </div>
</template>

<style scoped>
 .otherImg,img{
        width:250px;
        height:150px;
    }
    .other{
        display:flex;
        justify-content: center;
        flex-wrap: wrap;
        margin-top:50px
    }

    .singleOther{
        width:250px;
        display:flex;
        flex-direction:column;
        align-items: center;
        margin:5px
    }
    .singleOther p{
        width:80%;
        margin:auto
    }
    .otherWrapper{
            display: flex;
    flex-direction: column;
    align-items: center;
    }
    .otherTitle{
        width:100%;
        justify-content: flex-end;
        display:flex;
        margin-top:10px;
        font-size:11pt;
        font-weight:lighter
    }
    .otherTitle a{
        font-weight:bold
    }
    .otherTitle p{
        color:rgb(121, 121, 121);
    }
    .otherModel{
        display:flex;
        width:100%;
        justify-content:space-between;
        margin-top:10px;
        
    }
    .otherModel a{
        width:175px;
        text-align:right
    }
    .otherModel a{
        color:rgb(52, 52, 187)
    }
    svg {
        fill: none;
        stroke-width: 2px;
        stroke: #858585;
    }
    .otherModel button{
        border:0
    }
</style>