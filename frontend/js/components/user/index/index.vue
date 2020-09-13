<template>
  <div id="index" class="mainItemPerPage">
    <div id="topOfIndex" class="shouldCollapse">
      <div id="topOfIndexWrapper">
        <slider></slider>
        <categorie :mainCats="JSON.parse(main_categories)"></categorie>
      </div>
    </div>
    <div class="shouldCollapse">
      <comments></comments>
    </div>
	<div class="shouldCollapse">
		<flip-card></flip-card>
	</div>

    

    <!-- <expanding-card></expanding-card> -->

    <!-- <extra-sign-up></extra-sign-up> -->
    <div id="allCards" class="shouldCollapse maxIs">
      <card
        cardTitle="بیشترین کلیک شده"
        descs="فلان لان فلان خیلی فلا هی فلان بازم فلان"
        :products="JSON.parse(products)"
      ></card>
    </div>
    <div class="digiCardIndex shouldCollapse maxIs">
      <digi-card
        :imgs='JSON.stringify(["/images/shrink.png","/images/shrink2.png","/images/digi1.jpg","/images/digi2.jpg"])'
      ></digi-card>
      <customers></customers>
    </div>
  </div>
</template>
<script>
import digiCard from "./digiCard/digiCard.vue";
import slider from "./slider/slider.vue";
import card from "./card/card.vue";
import flipCard from "./flipCard/flipCard.vue";
import categorie from "./categorie/categorie.vue";
import expandingCard from "./expandingCard/expandingCard.vue";
import extraSignUp from "./extraSignUp/extraSignUp.vue";
import customers from "./customers/customers.vue"
import comments from "./comments/comments.vue"
export default {
  components: {
    slider,
    card,
    categorie,
    flipCard,
    digiCard,
    extraSignUp,
    expandingCard,
    customers,
    comments
  },
  props: ["products", "main_categories", "posts"],

  methods: {
    getProducts() {
      return JSON.stringify(this.products);
    },
  },
};
</script>

<style>
.shouldCollapse{
	width:90% !important;
}
.digiCardIndex {
  margin-top: 50px;
  margin-bottom: 20px;
}
#topOfIndex {
  background: #ffffff;
  width: 100%;
}
#topOfIndexWrapper {
  display: flex;
  justify-content: center;
  width: 100%;
  padding: 20px;
}
#index {
  position: relative;
}
#allCards {
  display: flex;
  width: 100%;
  flex-direction: column;
  align-items: center;
}
#mostClicked {
  grid-area: mostClicked;
}
#slider {
  grid-area: slide;
}
#new {
  grid-area: new;
}

#app {
  display: grid;
  width: 100%;
  grid-template-columns: repeat(2, 1fr);
  grid-template-rows: fit-content(1000rem) auto auto auto fit-content(1000rem);
  grid-template-areas:
    "header header"
    "slicer slicer"
    "navigation navigation"
    "main main"
    "footer footer";
}
.titleCard {
  display: flex;
  width: 100%;
  justify-content: flex-end;
}

#index {
  display: flex;
  flex-direction: column;
  align-items: center;
}

#flatMenu {
  grid-area: flatMenu;
}

.singleCard {
  background: white;
}

#footer {
  grid-area: footer;
}
.hamCats {
  grid-area: hamCats;
}
@media (max-width: 924px) {
  #slider {
    width: 100%;
  }
  #sideSliderCats {
    display: none;
  }
  .shouldCollapse{
	width:100% !important
}
}
@media (max-width: 800px) {
  #topOfIndexWrapper {
    padding: 0;
  }
}
</style>


