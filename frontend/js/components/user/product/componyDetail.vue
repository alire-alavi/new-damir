<template>
    <div id="componyDetail">
        <table>
            <tbody>
                <tr>
                    <td>1375</td>
                    <th>:سال تاسیس کمپانی</th>
                    
                    
                    
                </tr>
                <tr>
                    <td>تهران</td>
                    <th>:محل شرکت</th>
                    
                    
                    
                </tr>
                <tr>
                    <td>صوتی</td>
                    <th>:دسته بندی محصول</th>
                    
                    
                    
                </tr>
                <tr>
                    <td>30 تا 40 نفر</td>
                    <th>:تعداد کارمندان</th>
                    
                
                </tr>
            </tbody>
        </table>
    </div>
    
</template>

<style scoped>
#componyDetail{
    display:flex;
    justify-content: center;
}
    table{
        width: 95%;
        max-width: 100%;
        margin-bottom: 20px;
    }
    td{
        text-align:right;
        /* width:85% */
    }
    td,th{
        padding:10px
    }
    tr{
        border-top:1px solid rgb(191, 202, 202)
    }
    tr:nth-child(odd):hover{
        background: rgb(221, 215, 215);
    }
    th{
        text-align:right;
        width:max-content
    }
</style>