<template>
 <!-- Background Audio -->
 <audio ref="audioRef" loop>
 <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" type="audio/mpeg">
 </audio>

 <!-- Floating Music Toggle -->
 <MusicToggle :audioRef="audioRef" :isVisible="fullyOpened" />

 <!-- Antigravity Floating Particles -->
 <FloatingParticles v-if="fullyOpened" />

 <!-- Opening Shutter Overlay -->
 <div class="fixed inset-0 z-50 pointer-events-none flex flex-col" :class="{'hidden': fullyOpened}">
 <div class="bg-surface w-full h-1/2 flex items-end justify-center pb-8 transition-transform duration-[1.5s] ease-in-out pointer-events-auto z-20" :class="{'shutter-open-top': isOpened}">
 <h1 class="text-primary text-4xl md:text-6xl font-serif tracking-widest text-center" style="transform: translateY(50%)">
 ROMEO & JULIET
 </h1>
 </div>
 <div class="bg-surface w-full h-1/2 flex items-start justify-center pt-8 transition-transform duration-[1.5s] ease-in-out pointer-events-auto z-10" :class="{'shutter-open-bottom': isOpened}">
 <button @click="openInvitation" class="mt-12 px-8 py-3 bg-transparent border border-primary text-primary font-sans font-medium tracking-[0.2em] text-sm uppercase hover:bg-primary-container hover:text-on-primary-container hover:text-on-surface transition-all duration-500 hover:">
 Open Invitation
 </button>
 </div>
 </div>

 <!-- Main Scroll Container with perspective -->
 <div class="parallax-container" :class="{'overflow-hidden pointer-events-none h-screen': !isOpened}">
 <HeroSection />
 
 <div class="relative z-10 bg-surface ">
 <QuoteSection />
 <CoupleSection />
 <CountdownTimer />
 <EventDetails />
 <GallerySection />
 <GiftSection />
 <RSVPForm />
 
 <!-- Footer -->
 <footer class="py-16 bg-surface-container-low flex flex-col items-center justify-center">
 <h2 class="text-primary text-2xl font-serif tracking-widest mb-4">R & J</h2>
 <p class="text-on-surface text-xs font-sans tracking-[0.3em] opacity-60 uppercase mb-8">Thank you for your blessing</p>
 <p class="text-on-surface/30 text-[10px] font-sans tracking-widest">Built with Vue.js & Antigravity parralax</p>
 </footer>
 </div>
 </div>
</template>

<script setup>
import { ref } from 'vue';
import HeroSection from './components/HeroSection.vue'
import QuoteSection from './components/QuoteSection.vue'
import CoupleSection from './components/CoupleSection.vue'
import CountdownTimer from './components/CountdownTimer.vue'
import EventDetails from './components/EventDetails.vue'
import GallerySection from './components/GallerySection.vue'
import GiftSection from './components/GiftSection.vue'
import RSVPForm from './components/RSVPForm.vue'
import MusicToggle from './components/MusicToggle.vue'
import FloatingParticles from './components/FloatingParticles.vue'

const isOpened = ref(false)
const fullyOpened = ref(false)
const audioRef = ref(null)

const openInvitation = () => {
 isOpened.value = true
 if (audioRef.value) {
 audioRef.value.play().catch(e => console.log('Audio play failed:', e))
 }
 // Remove from DOM after transition completes to improve performance
 setTimeout(() => {
 fullyOpened.value = true
 }, 1500)
}
</script>
