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
        <div id="password" class="inputs">
          <div class="formInputsWrapper">
            <input
              autocomplete="off"
              name="password1"
              v-model="pass"
              @blur='focusOut($event),startValidation("phone",$event)'
              class="inputWithLabelThatShouldStay signupFormInputs"
              id="consulate"
              type="text"
            />
            <label class="comeUpLabel" for="consulate">شماره تلفن</label>
          </div>
          <p class="inputError">
            فرمت شماره تلفن اشتباه است
          </p>
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
      const res = this.validateUserInput(type, e);

      if (res) {
        error.style.visibility="hidden"
        return;
      }
      error.style.visibility="visible"
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
  bottom: -244.156px;
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
  background: #f6f6f4;
  margin: auto;
  padding: 10px;
  border: 1px solid #9f9f9f;
}
.sendReq {
  display: flex;
  justify-content: center;
  margin-top: 5px;
}
.title {
  background: rgb(0 116 217);
  padding: 10px;
  padding-bottom: 40px;
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
.inputError{
  display:block;
  visibility: hidden;
}
</style>