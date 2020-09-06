export const keepStay={
    methods:{
        focusOut(e){
            const input=e.target
            const label=input.nextElementSibling
            if(input.value!='')
            {
                label.classList.add("stay")
                return
            }
            label.classList.remove("stay")
        }
    }
}