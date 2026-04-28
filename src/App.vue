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
     <!-- Watercolor Background Layer (behind shutters) -->
     <div class="absolute inset-0 overflow-hidden">
       <!-- SVG Filters -->
       <svg class="absolute w-0 h-0" aria-hidden="true">
         <defs>
           <filter id="watercolor-filter">
             <feTurbulence
               id="turbulence"
               type="fractalNoise"
               baseFrequency="0.015"
               numOctaves="5"
               result="noise"
             />
             <feGaussianBlur in="noise" stdDeviation="3" result="blurredNoise" />
             <feDisplacementMap
               id="displacement"
               in="SourceGraphic"
               in2="blurredNoise"
               scale="80"
               xChannelSelector="R"
               yChannelSelector="G"
             />
           </filter>
         </defs>
       </svg>

       <!-- Watercolor Blobs -->
       <div class="absolute inset-0" :style="{ filter: 'url(#watercolor-filter)', mixBlendMode: 'multiply' }">
         <!-- Largest blob: Primary Watercolor #C08552 -->
         <div
           ref="mainBlob"
           class="absolute rounded-full"
           :style="mainBlobStyle"
         />
         <!-- Secondary blob: Deep Accent #8C5A3C -->
         <div
           class="absolute rounded-full"
           :style="secondaryBlobStyle"
         />
         <!-- Tertiary blob: Deep Accent #4B2E2B -->
         <div
           class="absolute rounded-full"
           :style="tertiaryBlobStyle"
         />
       </div>
     </div>

     <!-- Top Shutter -->
     <div class="bg-[#4B2E2B] w-full h-1/2 flex flex-col items-center justify-end pb-0 transition-transform duration-[1.5s] ease-in-out pointer-events-auto z-20" :class="{'shutter-open-top': isOpened}">
       <h1 class="text-black text-4xl md:text-6xl font-serif tracking-widest text-center mb-0">
         Adam & Hawa
       </h1>
       <img src="@/assets/Muslim Couple.svg" alt="Muslim Couple" class="w-32 md:w-48 opacity-80" style="transform: translateY(50%)" />
     </div>
     <!-- Bottom Shutter -->
     <div class="bg-[#4B2E2B] w-full h-1/2 flex flex-col items-center justify-start pt-4 transition-transform duration-[1.5s] ease-in-out pointer-events-auto z-10" :class="{'shutter-open-bottom': isOpened}">
       <button ref="btnRef" @mousemove="onMouseMove" @mouseleave="onMouseLeave" @click="openInvitation" class="mt-24 px-8 py-3 bg-transparent border border-primary text-black font-sans font-medium tracking-[0.2em] text-sm uppercase transition-colors duration-500 hover:bg-emerald-600 hover:text-white hover:border-emerald-600 shadow-lg hover:shadow-xl">
         Open Invitation
       </button>
     </div>
   </div>

   <!-- Main Scroll Container with perspective -->
   <div class="parallax-container min-h-screen bg-[#C08552]" :class="{'overflow-hidden pointer-events-none h-screen': !isOpened}">
   <HeroSection />
   
   <div class="relative z-10 bg-[#C08552]">
   <QuoteSection />
   <CoupleSection />
   <CountdownTimer />
   <EventDetails />
   <GallerySection />
   <GiftSection />
   <RSVPForm />
   
   <!-- Footer -->
     <footer class="py-16 bg-surface-container-low flex flex-col items-center justify-center">
     <h2 class="text-black text-2xl font-serif tracking-widest mb-4">R & J</h2>
     <p class="text-on-surface text-xs font-sans tracking-[0.3em] opacity-60 uppercase mb-8">Thank you for your blessing</p>
     <p class="text-on-surface/30 text-[10px] font-sans tracking-widest">Built with Vue.js & Antigravity parralax</p>
     </footer>
   </div>
   </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import gsap from 'gsap';

// Watercolor blob reactive styles
const mainBlobStyle = ref({
  background: 'radial-gradient(circle at 50% 50%, #C08552, rgba(192, 133, 82, 0.1))',
  width: '0px',
  height: '0px',
  left: '50%',
  top: '50%',
  transform: 'translate(-50%, -50%)',
  borderRadius: '50%',
})

const secondaryBlobStyle = ref({
  background: 'radial-gradient(circle at 60% 40%, #8C5A3C, rgba(140, 90, 60, 0.08))',
  width: '0px',
  height: '0px',
  left: '60%',
  top: '40%',
  transform: 'translate(-50%, -50%)',
  borderRadius: '50%',
})

const tertiaryBlobStyle = ref({
  background: 'radial-gradient(circle at 40% 60%, #4B2E2B, rgba(75, 46, 43, 0.06))',
  width: '0px',
  height: '0px',
  left: '40%',
  top: '60%',
  transform: 'translate(-50%, -50%)',
  borderRadius: '50%',
})

const isOpened = ref(false)
const fullyOpened = ref(false)
const audioRef = ref(null)
const btnRef = ref(null)
const mainBlob = ref(null)
let watercolorTimeline = null

onMounted(() => {
  // Gentle pulse animation for the button to invite clicks
  if (btnRef.value) {
    gsap.fromTo(btnRef.value, 
      { y: 10, opacity: 0 },
      { y: 0, opacity: 1, duration: 1.5, ease: 'power3.out', delay: 0.5 }
    );
    
    gsap.to(btnRef.value, {
      scale: 1.05,
      duration: 1.5,
      repeat: -1,
      yoyo: true,
      ease: 'sine.inOut'
    });
  }

  // Watercolor entrance animation on mount
  initWatercolorAnimation()
})

const initWatercolorAnimation = () => {
  watercolorTimeline = gsap.timeline()

  // Animate main blob (#C08552) to fill screen gradually
  watercolorTimeline.to(mainBlobStyle.value, {
    width: '200vmax',
    height: '200vmax',
    duration: 2.5,
    ease: 'power2.out'
  }, 0)

  // Secondary blob appears
  watercolorTimeline.to(secondaryBlobStyle.value, {
    width: '150vmax',
    height: '150vmax',
    duration: 2,
    ease: 'power2.out'
  }, 0.3)

  // Tertiary blob appears
  watercolorTimeline.to(tertiaryBlobStyle.value, {
    width: '180vmax',
    height: '180vmax',
    duration: 2.2,
    ease: 'power2.out'
  }, 0.5)

  // Animate SVG displacement filter settling (wet → dry effect)
  watercolorTimeline.to('#displacement', {
    attr: { scale: 25 },
    duration: 5,
    ease: 'power1.inOut'
  }, 0)
}

const onMouseMove = (e) => {
  if (!btnRef.value) return;
  const rect = btnRef.value.getBoundingClientRect();
  const x = (e.clientX - rect.left - rect.width / 2) * 0.3;
  const y = (e.clientY - rect.top - rect.height / 2) * 0.3;
  
  gsap.to(btnRef.value, {
    x: x,
    y: y,
    duration: 0.3,
    ease: "power2.out"
  });
};

const onMouseLeave = () => {
  if (!btnRef.value) return;
  gsap.to(btnRef.value, {
    x: 0,
    y: 0,
    duration: 0.7,
    ease: "elastic.out(1, 0.3)"
  });
};

const openInvitation = () => {
  // Stop button pulse animation
  if (btnRef.value) gsap.killTweensOf(btnRef.value);

  // Let watercolor settle partially before opening shutters
  // Pause the ongoing watercolor timeline and fast-forward to a settled state
  if (watercolorTimeline) {
    // Progress timeline to 60% (wash has mostly filled and settled)
    watercolorTimeline.progress(0.6)
    // Pause further animation
    watercolorTimeline.pause()
  }

  // Trigger shutter open animation
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
