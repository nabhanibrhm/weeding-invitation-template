<template>
 <section class="py-24 md:py-32 bg-surface relative w-full overflow-hidden" ref="sectionRef">
 <div class="container mx-auto px-6 max-w-6xl">
 <div class="text-center mb-16 md:mb-24 transition-all duration-1000 transform" :class="isVisible ? 'translate-y-0 opacity-100' : 'translate-y-10 opacity-0'">
 <p class="text-primary text-xs tracking-[0.3em] uppercase mb-4">When & Where</p>
 <h2 class="text-3xl md:text-5xl font-serif text-on-surface mb-4">Event Details</h2>
 
 </div>

 <div class="flex flex-col lg:flex-row gap-12 lg:gap-8 items-stretch">
 
 <!-- details cards -->
 <div class="w-full lg:w-1/2 flex flex-col gap-6 md:gap-8">
 
 <!-- Holy Matrimony -->
 <div class="glass-panel p-8 md:p-12 border border-primary/5 transition-all duration-1000 transform group hover:-translate-y-1" :class="isVisible ? 'translate-x-0 opacity-100' : '-translate-x-10 opacity-0'" style="transition-delay: 200ms;">
 <h3 class="text-2xl font-serif text-on-surface mb-2">Holy Matrimony</h3>
 <p class="text-primary font-sans text-sm tracking-widest uppercase mb-6">Ceremony</p>
 
 <div class="space-y-4 mb-8 text-sm md:text-base font-sans text-on-surface/80">
 <div class="flex items-start">
 <span class="w-6 inline-block mr-3 text-primary">•</span>
 <span>Saturday, October 24th, 2026</span>
 </div>
 <div class="flex items-start">
 <span class="w-6 inline-block mr-3 text-primary">•</span>
 <span>10:00 AM - 11:30 AM</span>
 </div>
 </div>
 
 <p class="font-sans text-xs tracking-widest text-on-surface uppercase mb-2">Venue</p>
 <p class="font-serif text-lg text-on-surface mb-1">Cathedral of The Good Shepherd</p>
 <p class="font-sans text-sm text-on-surface/60 leading-relaxed">
 Queen St, Singapore
 </p>
 </div>

 <!-- Reception -->
 <div class="glass-panel p-8 md:p-12 border border-primary/5 transition-all duration-1000 transform group hover:-translate-y-1" :class="isVisible ? 'translate-x-0 opacity-100' : '-translate-x-10 opacity-0'" style="transition-delay: 400ms;">
 <h3 class="text-2xl font-serif text-on-surface mb-2">Wedding Reception</h3>
 <p class="text-primary font-sans text-sm tracking-widest uppercase mb-6">Celebration</p>
 
 <div class="space-y-4 mb-8 text-sm md:text-base font-sans text-on-surface/80">
 <div class="flex items-start">
 <span class="w-6 inline-block mr-3 text-primary">•</span>
 <span>Saturday, October 24th, 2026</span>
 </div>
 <div class="flex items-start">
 <span class="w-6 inline-block mr-3 text-primary">•</span>
 <span>06:00 PM - 10:00 PM</span>
 </div>
 </div>
 
 <p class="font-sans text-xs tracking-widest text-on-surface uppercase mb-2">Venue</p>
 <p class="font-serif text-lg text-on-surface mb-1">The Ritz-Carlton, Millenia</p>
 <p class="font-sans text-sm text-on-surface/60 leading-relaxed">
 Grand Ballroom<br/>Marina Bay, Singapore
 </p>
 </div>

 </div>

 <!-- maps -->
 <div class="w-full lg:w-1/2 glass-panel p-2 border border-primary/10 transition-all duration-1000 transform" :class="isVisible ? 'translate-x-0 opacity-100' : 'translate-x-10 opacity-0'" style="transition-delay: 600ms;">
 <div class="w-full h-[300px] lg:h-full min-h-[400px] relative filter grayscale hover:grayscale-0 transition-all duration-700">
 <iframe 
 src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3988.7909362391035!2d103.85764021111666!3d1.2917751987018318!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31da19afe06ce607%3A0xc6cb12b2a6adbae7!2sThe%20Ritz-Carlton%2C%20Millenia%20Singapore!5e0!3m2!1sen!2sid!4v1714412234567!5m2!1sen!2sid" 
 width="100%" height="100%" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade" class="absolute inset-0">
 </iframe>
 </div>
 </div>

 </div>
 </div>
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
 }
 })
 }, { threshold: 0.1 })
 
 if (sectionRef.value) observer.observe(sectionRef.value)
})

onUnmounted(() => {
 if (observer && sectionRef.value) observer.unobserve(sectionRef.value)
})
</script>
