<template>
 <section class="py-24 md:py-32 relative overflow-hidden bg-surface" ref="sectionRef">
 <div class="container mx-auto px-6 max-w-5xl">
 <div class="text-center mb-20 md:mb-32">
 <h2 class="text-3xl md:text-5xl font-serif text-on-surface mb-4">Groom & Bride</h2>
 
 </div>

 <div class="flex flex-col md:flex-row items-center justify-between gap-16 md:gap-8">
 <!-- Groom -->
 <div class="w-full md:w-5/12 flex flex-col items-center glass-panel rounded-3xl p-8 md:items-end text-center md:text-right transition-all duration-[1.5s] ease-out transform"
 :class="isVisible ? 'translate-x-0 opacity-100' : '-translate-x-32 opacity-0'">
 <div class="relative w-64 h-80 md:w-72 md:h-96 mb-8 group">
 <div class="absolute inset-0 border border-primary translate-x-4 translate-y-4 -x-2 -y-2 transition-transform duration-500 z-0"></div>
 <img src="@/assets/couple.png" alt="Groom" class="absolute inset-0 w-full h-full object-cover object-[center_20%] z-10 " />
 </div>
 <h3 class="text-2xl md:text-3xl font-serif text-on-surface mb-2">Romeo Montague</h3>
 <p class="text-sm font-sans tracking-[0.1em] text-primary uppercase mb-4">The Groom</p>
 <p class="text-sm text-on-surface/70 leading-relaxed font-sans max-w-xs">
 Son of Mr. Montague & Mrs. Montague<br/>
 "Forever is composed of nows."
 </p>
 </div>

 <!-- Divider / "&" -->
 <div class="w-full md:w-2/12 flex justify-center text-primary text-6xl md:text-8xl font-serif italic opacity-30 transform transition-all duration-1000 delay-500"
 :class="isVisible ? 'scale-100 opacity-30' : 'scale-50 opacity-0'">
 &
 </div>

 <!-- Bride -->
 <div class="w-full md:w-5/12 flex flex-col items-center glass-panel rounded-3xl p-8 md:items-start text-center md:text-left transition-all duration-[1.5s] ease-out transform delay-300"
 :class="isVisible ? 'translate-x-0 opacity-100' : 'translate-x-32 opacity-0'">
 <div class="relative w-64 h-80 md:w-72 md:h-96 mb-8 group">
 <div class="absolute inset-0 border border-primary -translate-x-4 -translate-y-4 group-hover:-translate-x-2 group-hover:-translate-y-2 transition-transform duration-500 z-0"></div>
 <img src="@/assets/couple.png" alt="Bride" class="absolute inset-0 w-full h-full object-cover object-[center_30%] z-10 " />
 </div>
 <h3 class="text-2xl md:text-3xl font-serif text-on-surface mb-2">Juliet Capulet</h3>
 <p class="text-sm font-sans tracking-[0.1em] text-primary uppercase mb-4">The Bride</p>
 <p class="text-sm text-on-surface/70 leading-relaxed font-sans max-w-xs">
 Daughter of Mr. Capulet & Mrs. Capulet<br/>
 "My bounty is as boundless as the sea."
 </p>
 </div>
 </div>
 </div>
 
 <!-- Decorative floating elements -->
 <div class="absolute top-20 right-[-10%] w-64 h-64 border border-primary/10 rounded-full animate-float hidden md:block"></div>
 <div class="absolute bottom-10 left-[-10%] w-48 h-48 border border-primary/10 rounded-full animate-float" style="animation-delay: 2s; animation-duration: 12s;"></div>
 </section>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const isVisible = ref(false)
const sectionRef = ref(null)

let observer

onMounted(() => {
 observer = new IntersectionObserver((entries) => {
 entries.forEach(entry => {
 if (entry.isIntersecting) {
 isVisible.value = true
 // Optional: unobserve after showing once
 // observer.unobserve(entry.target)
 }
 })
 }, {
 threshold: 0.2
 })
 
 if (sectionRef.value) {
 observer.observe(sectionRef.value)
 }
})

onUnmounted(() => {
 if (observer && sectionRef.value) {
 observer.unobserve(sectionRef.value)
 }
})
</script>
