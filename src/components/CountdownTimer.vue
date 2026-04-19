<template>
  <section class="py-20 md:py-32 bg-mulyo-charcoal relative text-mulyo-cream overflow-hidden" ref="sectionRef">
    <!-- Decorative background elements -->
    <div class="absolute inset-0 opacity-10">
      <div class="absolute top-0 left-10 w-[300px] h-[300px] bg-mulyo-gold rounded-full blur-[100px]"></div>
      <div class="absolute bottom-0 right-10 w-[200px] h-[200px] bg-white rounded-full blur-[80px]"></div>
    </div>
    
    <div class="container mx-auto px-6 relative z-10 flex flex-col items-center justify-center">
      <p class="text-mulyo-gold text-xs tracking-[0.3em] uppercase mb-4 animate-fade-in">Save The Date</p>
      <h2 class="text-3xl md:text-5xl font-playfair mb-16 text-center">Counting down to our forever</h2>
      
      <div class="flex flex-wrap justify-center gap-4 md:gap-8 lg:gap-12"
           :class="isVisible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-20'"
           style="transition: all 1s ease-out;">
        
        <!-- Days -->
        <div class="flex flex-col items-center">
          <div class="w-16 h-16 md:w-24 md:h-24 lg:w-28 lg:h-28 rounded-full border border-mulyo-gold/30 flex items-center justify-center bg-white/5 backdrop-blur-sm shadow-[0_0_15px_rgba(212,175,55,0.1)] mb-4">
            <span class="text-2xl md:text-4xl lg:text-5xl font-playfair">{{ days }}</span>
          </div>
          <span class="text-[10px] md:text-xs tracking-[0.2em] uppercase text-mulyo-cream/60">Days</span>
        </div>
        
        <div class="text-xl md:text-3xl font-playfair text-mulyo-gold mt-[18px] md:mt-[24px] lg:mt-[30px]">:</div>
        
        <!-- Hours -->
        <div class="flex flex-col items-center">
          <div class="w-16 h-16 md:w-24 md:h-24 lg:w-28 lg:h-28 rounded-full border border-mulyo-gold/30 flex items-center justify-center bg-white/5 backdrop-blur-sm shadow-[0_0_15px_rgba(212,175,55,0.1)] mb-4">
            <span class="text-2xl md:text-4xl lg:text-5xl font-playfair">{{ hours }}</span>
          </div>
          <span class="text-[10px] md:text-xs tracking-[0.2em] uppercase text-mulyo-cream/60">Hours</span>
        </div>
        
        <div class="text-xl md:text-3xl font-playfair text-mulyo-gold mt-[18px] md:mt-[24px] lg:mt-[30px]">:</div>
        
        <!-- Minutes -->
        <div class="flex flex-col items-center">
          <div class="w-16 h-16 md:w-24 md:h-24 lg:w-28 lg:h-28 rounded-full border border-mulyo-gold/30 flex items-center justify-center bg-white/5 backdrop-blur-sm shadow-[0_0_15px_rgba(212,175,55,0.1)] mb-4">
            <span class="text-2xl md:text-4xl lg:text-5xl font-playfair">{{ minutes }}</span>
          </div>
          <span class="text-[10px] md:text-xs tracking-[0.2em] uppercase text-mulyo-cream/60">Minutes</span>
        </div>
        
        <div class="text-xl md:text-3xl font-playfair text-mulyo-gold mt-[18px] md:mt-[24px] lg:mt-[30px]">:</div>
        
        <!-- Seconds -->
        <div class="flex flex-col items-center">
          <div class="w-16 h-16 md:w-24 md:h-24 lg:w-28 lg:h-28 rounded-full border border-mulyo-gold/30 flex items-center justify-center bg-white/5 backdrop-blur-sm shadow-[0_0_15px_rgba(212,175,55,0.1)] mb-4">
             <span class="text-2xl md:text-4xl lg:text-5xl font-playfair">{{ seconds }}</span>
          </div>
          <span class="text-[10px] md:text-xs tracking-[0.2em] uppercase text-mulyo-cream/60">Seconds</span>
        </div>
        
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const targetDate = new Date('2026-10-24T18:00:00').getTime()

const days = ref('00')
const hours = ref('00')
const minutes = ref('00')
const seconds = ref('00')

const isVisible = ref(false)
const sectionRef = ref(null)

let timer
let observer

const updateCountdown = () => {
  const now = new Date().getTime()
  const distance = targetDate - now

  if (distance < 0) {
    clearInterval(timer)
    return
  }

  const d = Math.floor(distance / (1000 * 60 * 60 * 24))
  const h = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60))
  const m = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60))
  const s = Math.floor((distance % (1000 * 60)) / 1000)

  days.value = d < 10 ? '0' + d : d
  hours.value = h < 10 ? '0' + h : h
  minutes.value = m < 10 ? '0' + m : m
  seconds.value = s < 10 ? '0' + s : s
}

onMounted(() => {
  updateCountdown()
  timer = setInterval(updateCountdown, 1000)
  
  observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        isVisible.value = true
      }
    })
  }, { threshold: 0.3 })
  
  if (sectionRef.value) observer.observe(sectionRef.value)
})

onUnmounted(() => {
  clearInterval(timer)
  if (observer && sectionRef.value) observer.unobserve(sectionRef.value)
})
</script>
