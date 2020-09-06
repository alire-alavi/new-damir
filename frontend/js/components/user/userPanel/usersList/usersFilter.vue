<template>
  <div id="usersSearch">
    <div class="searchBarBtn">
      <button @click='isShow=!isShow' class="done">فیلتر مشتریان</button>
    </div>
    <transition name="searchBar">
      <div class="searchBarItems" v-if='isShow'>
        <div class="searchPrice">
          <label class="title" for>بر اساس قیمت</label>
          <div class="choices">
            <div class="choicesWrapper">
              <div class="singleChoice">
                <input type="radio" name="price" value="most" id />
                <label for>کمترین</label>
              </div>
              <div class="singleChoice">
                <input type="radio" name="price" value="least" id />
                <label for>بیشترین</label>
              </div>
            </div>
          </div>
        </div>

        <div class="searchPrice">
          <label class="title" for>بر اساس زمان</label>
          <div class="choices">
            <div class="choicesWrapper">
              <div class="singleChoice">
                <input type="radio" name="time" value="oldest" id />
                <label for>قدیمی ترین</label>
              </div>
              <div class="singleChoice">
                <input type="radio" name="time" value="newest" id />
                <label for>جدیدترین</label>
              </div>
            </div>
          </div>
        </div>

        <div class="searchPrice">
          <label class="title" for>بر اساس زمان مشخص</label>
          <div class="choices">
            <div class="choicesWrapper datePicker">
              <div class="singleChoice">
                <date-picker
                  class="datePickerComp"
                  v-model="from"
                  label="از تاریخ"
                  :clearable="true"
                ></date-picker>
              </div>
              <div class="singleChoice">
                <date-picker class="datePickerComp" v-model="to" label="تا تاریخ" :clearable="true"></date-picker>
              </div>
            </div>
          </div>
        </div>
        <div class="searchFilterSubmit">
            <button class='danger'>فیلتر</button>
        </div>
      </div>
      
    </transition>
  </div>
</template>

<script>
import datePicker from "vue-persian-datetime-picker";
export default {
  components: {
    datePicker,
  },
  data() {
    return {
      from: null,
      to: null,
      isShow:false
    };
  },
};
</script>


<style scoped>
.searchBarItems{
    padding:20px;
    margin-top:20px;
    background: rgb(212, 196, 208);
}
.searchFilterSubmit{
    display:flex;
    justify-content: center;
}
input {
  color: black !important;
}
.datePicker {
  display: flex;
  flex-direction: column;
}
.datePickerComp {
  margin-top: 10px;
}
.title {
  background: rgb(50, 25, 189);
  color: white;
  font-size: 15pt;
  padding: 10px;
  border-top-left-radius: 10px;
  border-bottom-left-radius: 10px;
}
.choices {
  margin-top: 10px;
}
#usersSearch {
  margin-top: 20px;
}
.searchPrice {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  flex-wrap: wrap;
  margin-top: 10px;
}
.choicesWrapper {
  display: flex;
}
.singleChoice {
  display: flex;
  align-items: center;
}
.searchBar-enter-active{
    animation:comIn 0.5s linear forwards
}
.searchBar-leave-active{
    animation:comOut 0.5s linear forwards
}
@keyframes comIn {
    from{
        opacity: 0;
        transform:translateX(100%)
    }
    to{
        opacity: 1;
        transform:translateX(0)
    }
}
@keyframes comOut {
    from{
        opacity: 1;
        transform:translateX(0)
    }
    to{
        opacity: 0;
        transform:translateX(100%)
    }
}
</style>
