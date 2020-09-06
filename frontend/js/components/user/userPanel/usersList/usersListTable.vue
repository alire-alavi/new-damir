<template>
        <transition name='slide'>
            <div id="table">
                <table>
                    <tr>
                        <th>نام</th>
                        <th>ایمیل</th>
                        <th>شرکت</th>
                        <th>شماره تلفن</th>
                    </tr>
                    <tr>
                        <td>john.doe</td>
                        <td>john.doe@gmail.com</td>
                        <td>دمیر کو</td>
                        <td>09367134752</td>
                        <td><button class='danger'>حذف کاربر</button></td>
                    </tr>
                    <tr>
                        <td>john.doe</td>
                        <td>john.doe@gmail.com</td>
                        <td>دمیر کو</td>
                        <td>09367134752</td>
                        <td><button class='danger'>حذف کاربر</button></td>
                    </tr>
                    <tr>
                        <td>john.doe</td>
                        <td>john.doe@gmail.com</td>
                        <td>دمیر کو</td>
                        <td>09367134752</td>
                        <td><button class='danger'>حذف کاربر</button></td>
                    </tr>
                    <tr>
                        <td>john.doe</td>
                        <td>john.doe@gmail.com</td>
                        <td>دمیر کو</td>
                        <td>09367134752</td>
                        <td><button class='danger'>حذف کاربر</button></td>
                    </tr>
                </table>
            </div>
        </transition>

</template>


<style scoped>
    tr:nth-child(even){background-color: #dad8d8;}
    #table{
        overflow-x:scroll;
        margin-top:20px;
        max-width: 100%;
        transition: all 1s;
    }
    table{
        
        width:max-content;
        margin:auto        
    }
    th,td{
        text-align: center;
        padding-top: 12px;
        padding-bottom: 12px;
        border:1px solid rgb(179, 179, 179);
        padding:20px;
        max-width:100%
    }
    th{
        background: #4CAF50;
    }
    @keyframes slide {
        from{
            transform:translateY(20px)
        }
        to{
            transform:translateY(0)
        }
    }


</style>