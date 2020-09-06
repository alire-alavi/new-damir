<template>
  <div class="consulate">
    <div class="title">
      <p>درخواست مشاوره رایگان</p>
    </div>
    <div class="consulateWrapper">
      <form action>
        <div id="name" class="inputs">
          <div class="formInputsWrapper">
            <input
              autocomplete="off"
              @blur="focusOut($event)"
              class="signupFormInputs inputWithLabelThatShouldStay"
              id="name"
              type="text"
            />
            <label class="comeUpLabel" for="name">نام</label>
          </div>
        </div>
        <div id="email" class="inputs">
          <div class="formInputsWrapper">
            <input
              autocomplete="off"
              @blur="focusOut($event),startValidation('phone',$event)"
              class="signupFormInputs inputWithLabelThatShouldStay"
              id="userEmail"
              type="text"
            />
            <label class="comeUpLabel" for="userEmail">شماره تلفن همراه</label>
          </div>
          <p class="inputError">فرمت شماره اشتباه است</p>
        </div>
        <div class="sendReq">
          <button
            @click.prevent="sendConsulateRequest"
            class="sendConsulateRequest submit"
          >ثبت درخواست</button>
          <loading class="consulateLoading"></loading>
        </div>
      </form>
    </div>
    <transition name="done" mode="out-in">
      <done-message></done-message>
    </transition>
  </div>
</template>

<script>
import { keepStay } from "../../user/mixIns/keepStay.js";
import doneMessage from "../../user/template/doneMessage/doneMessage.vue";
import { validationRules } from "../../user/mixIns/validationMixIn.js";
import { toggleDoneMessage } from "../../user/mixIns/doneMessageToggle.js";
import loading from "../../user/loading/loading.vue";
export default {
  mixins: [keepStay, validationRules, toggleDoneMessage],
  components: {
    doneMessage,
    loading,
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
    sendConsulateRequest() {
      const btn = document.querySelector(".sendConsulateRequest");
      btn.style.display = "none";
      const loading = document.querySelector(".consulateLoading");
      loading.style.display = "block";

      setTimeout(() => {
        this.toggleDoneMessage();
        btn.style.display = "block";
        loading.style.display = "none";
      }, 2000);
    },
  },
};
</script>

<style scoped>
.consulate {
  position: fixed;
  right: 50px;
  bottom: -237.156px;
  transition: all 0.5s linear;
  z-index: 667;
}
.consulate:hover {
  bottom: 0;
}
.formInputsWrapper {
  display: flex;
  justify-content: center;
}
.consulateWrapper {
  background: rgb(173, 166, 176);
  margin: auto;
  padding: 10px;
}
.sendReq {
  display: flex;
  justify-content: center;
  margin-top: 5px;
}
.title {
  background: rgb(229, 46, 113);
  padding: 10px;
  border-top-left-radius: 10px;
  border-top-right-radius: 10px;
  cursor: pointer;
}
.inputs {
  margin-top: 5px;
  display: flex;
  justify-content: center;
  flex-direction: column;
  align-items: center;
}
.inputError {
  font-size: 14pt;
}
.loading {
  width: 148px;
  height: 50px;
  margin: 0;
  display: none;
}
</style>