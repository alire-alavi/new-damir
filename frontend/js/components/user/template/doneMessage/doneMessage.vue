<template>
    <div id="doneMessage">
        <div id="doneMessageWrapper">
            <img src="/images/check.png" alt="">
            <p>درخواست شما با موفقیت انجام شد</p>
        </div>
    </div>
</template>

<style scoped>
    #doneMessage{
        display:none;
        position: fixed;
        right:20px;
        top:50px;
        background: rgb(51,188,70);
        color:black;
        border-radius: 5px;
        z-index: 20000;
        animation :comeIn 0.5s linear
    }
    @keyframes comeIn {
        0%{
            right:-100%;
            transform:rotateZ(180deg)
        }
        100%{
            right:20px;
            transform: rotateZ(0);
        }
    }
    #doneMessageWrapper{
        display:flex;
        padding:20px;
        align-items: center;
    }
    p{
        font-size:15pt
    }
    img{
        width:40px;
        height:40px;
    }
    
</style>