<template>
    <div id="technicalDetail">
        <table>
            <tbody>
                <tr>
                    
                    <td>فولاد</td>
                    <th>:جنس</th>
                    
                    
                </tr>
                <tr>
                    
                    <td>150 کیلو</td>
                    <th>:وزن</th>
                    
                    
                </tr>
                <tr>
                    
                    <td>1000 در دقیقه</td>
                    <th>:سرعت</th>
                    
                    
                </tr>
            </tbody>
        </table>
    </div>
    
</template>

<style scoped>
#technicalDetail{
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