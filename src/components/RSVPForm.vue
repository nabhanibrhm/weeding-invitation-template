<template>
  <section class="py-24 md:py-32 relative bg-[url('@/assets/hero_bg.png')] bg-cover bg-center bg-fixed text-mulyo-charcoal" ref="sectionRef">
    <div class="absolute inset-0 bg-mulyo-cream/80 backdrop-blur-sm"></div>
    
    <div class="container mx-auto px-6 relative z-10 max-w-3xl">
      <div class="text-center mb-12 md:mb-16 transition-all duration-1000 transform" :class="isVisible ? 'translate-y-0 opacity-100' : 'translate-y-10 opacity-0'">
        <h2 class="text-3xl md:text-5xl font-playfair mb-4">Are you attending?</h2>
        <p class="text-sm md:text-base font-sans tracking-widest text-mulyo-charcoal/70 uppercase">Please RSVP by September 24, 2026</p>
      </div>
      
      <!-- Glassmorphism Form -->
      <form @submit.prevent="submitRSVP" class="glass-panel rounded-lg p-8 md:p-12 transition-all duration-1000 transform delay-300" :class="isVisible ? 'translate-y-0 opacity-100' : 'translate-y-10 opacity-0'">
        
        <div class="mb-8 relative">
          <input type="text" id="name" v-model="form.name" required placeholder=" " 
                 class="w-full bg-transparent border-0 border-b border-mulyo-charcoal/30 text-mulyo-charcoal font-sans py-3 px-2 focus:ring-0 focus:border-mulyo-gold transition-colors peer placeholder-transparent outline-none">
          <label for="name" class="absolute left-2 top-3 text-mulyo-charcoal/50 font-sans tracking-widest text-xs uppercase -translate-y-7 scale-75 origin-[0] peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-7 transition-all duration-300">Full Name</label>
        </div>
        
        <div class="mb-8 relative">
          <input type="number" id="guests" v-model="form.guests" required min="1" max="5" placeholder=" "
                 class="w-full bg-transparent border-0 border-b border-mulyo-charcoal/30 text-mulyo-charcoal font-sans py-3 px-2 focus:ring-0 focus:border-mulyo-gold transition-colors peer placeholder-transparent outline-none">
          <label for="guests" class="absolute left-2 top-3 text-mulyo-charcoal/50 font-sans tracking-widest text-xs uppercase -translate-y-7 scale-75 origin-[0] peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-7 transition-all duration-300">Number of Guests</label>
        </div>
        
        <div class="mb-10">
          <p class="text-xs font-sans tracking-widest text-mulyo-charcoal/50 uppercase mb-4 pl-2">Will you attend?</p>
          <div class="flex gap-6 pl-2 font-sans text-sm">
            <label class="flex items-center cursor-pointer group">
              <input type="radio" v-model="form.attending" value="yes" class="hidden">
              <div class="w-4 h-4 rounded-full border border-mulyo-charcoal mr-2 flex items-center justify-center transition-all" :class="{'border-mulyo-gold bg-mulyo-gold shadow-[0_0_10px_rgba(212,175,55,0.4)]': form.attending === 'yes'}">
                <div class="w-1.5 h-1.5 rounded-full bg-white transition-opacity" :class="form.attending === 'yes' ? 'opacity-100' : 'opacity-0'"></div>
              </div>
              <span class="group-hover:text-mulyo-gold transition-colors">Joyfully Accept</span>
            </label>
            <label class="flex items-center cursor-pointer group">
              <input type="radio" v-model="form.attending" value="no" class="hidden">
              <div class="w-4 h-4 rounded-full border border-mulyo-charcoal mr-2 flex items-center justify-center transition-all" :class="{'border-mulyo-gold bg-mulyo-gold shadow-[0_0_10px_rgba(212,175,55,0.4)]': form.attending === 'no'}">
                <div class="w-1.5 h-1.5 rounded-full bg-white transition-opacity" :class="form.attending === 'no' ? 'opacity-100' : 'opacity-0'"></div>
              </div>
              <span class="group-hover:text-mulyo-gold transition-colors">Regretfully Decline</span>
            </label>
          </div>
        </div>

        <div class="mb-10 relative">
          <textarea id="message" v-model="form.message" placeholder=" " rows="2"
                 class="w-full bg-transparent border-0 border-b border-mulyo-charcoal/30 text-mulyo-charcoal font-sans py-2 px-2 focus:ring-0 focus:border-mulyo-gold transition-colors peer placeholder-transparent outline-none resize-none"></textarea>
          <label for="message" class="absolute left-2 top-2 text-mulyo-charcoal/50 font-sans tracking-widest text-xs uppercase -translate-y-7 scale-75 origin-[0] peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-7 transition-all duration-300">Wishes for the couple</label>
        </div>
        
        <div class="text-center mt-12">
          <button type="submit" class="px-12 py-4 bg-mulyo-charcoal text-mulyo-gold font-sans font-medium tracking-widest text-xs uppercase hover:bg-black transition-all duration-300 shadow-xl hover:shadow-[0_10px_20px_rgba(0,0,0,0.2)]">
            Send RSVP
          </button>
        </div>
        
        <!-- Success State -->
        <div v-if="submitted" class="absolute inset-0 bg-white/90 backdrop-blur-md rounded-lg flex flex-col items-center justify-center p-8 text-center animate-fade-in z-20">
          <div class="w-16 h-16 rounded-full border border-mulyo-gold flex items-center justify-center text-mulyo-gold mb-6 shadow-[0_0_20px_rgba(212,175,55,0.2)]">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
            </svg>
          </div>
          <h3 class="text-2xl font-playfair mb-2">Thank You</h3>
          <p class="font-sans text-sm text-mulyo-charcoal/70 tracking-widest uppercase mb-6 max-w-xs leading-relaxed">Your message has been received.</p>
          <button @click="submitted = false; form.message = ''" class="text-xs uppercase tracking-widest text-mulyo-gold border-b border-mulyo-gold pb-1 hover:text-mulyo-charcoal hover:border-mulyo-charcoal transition-all">Close</button>
        </div>
      </form>
    </div>
  </section>
</template>

<script setup>
import { ref, reactive, onMounted, onUnmounted } from 'vue'

const isVisible = ref(false)
const sectionRef = ref(null)
const submitted = ref(false)

const form = reactive({
  name: '',
  guests: '1',
  attending: 'yes',
  message: ''
})

let observer

onMounted(() => {
  observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        isVisible.value = true
      }
    })
  }, { threshold: 0.1 })
  
  if (sectionRef.value) observer.observe(sectionRef.value)
})

onUnmounted(() => {
  if (observer && sectionRef.value) observer.unobserve(sectionRef.value)
})

const submitRSVP = () => {
  // Simulate API call
  setTimeout(() => {
    submitted.value = true
  }, 500)
}
</script>
