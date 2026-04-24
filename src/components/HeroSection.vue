<template>
 <section 
 ref="sectionRef" 
 class="relative min-h-screen flex flex-col items-center justify-center overflow-hidden bg-surface"
 >
 <!-- Background Wrapper -->
 <div 
 ref="bgRef" 
 class="absolute inset-0 w-full h-full origin-center"
 >
 <div class="w-full h-full bg-[url('@/assets/hero_bg.png')] bg-cover bg-center mix-blend-multiply opacity-40"></div>
 <div class="absolute inset-0 bg-gradient-to-t from-surface via-transparent to-transparent opacity-80"></div>
 </div>
 
 <!-- Ornaments -->
 <!-- Top Left Ornament -->
 <div 
 ref="ornamentTopLeftRef" 
 class="absolute top-10 left-10 w-24 h-24 md:w-40 md:h-40 opacity-0 invisible"
 >
 <img src="../assets/icon_shapes_14.svg" alt="floral ornament" class="w-full h-full object-contain mix-blend-multiply opacity-80" />
 </div>

 <!-- Bottom Right Ornament -->
 <div 
 ref="ornamentBottomRightRef" 
 class="absolute bottom-10 right-10 w-24 h-24 md:w-40 md:h-40 rotate-[180deg] opacity-0 invisible"
 >
 <img src="../assets/icon_shapes_14.svg" alt="floral ornament" class="w-full h-full object-contain mix-blend-multiply opacity-80" />
 </div>

 <!-- Content Card -->
 <div class="relative z-10 flex flex-col items-center justify-center text-center px-4 w-full">
 <div ref="el => { if(el) textRefs[0] = el }" class="opacity-0 invisible">
 <p class="text-primary tracking-[0.4em] text-xs md:text-sm font-sans font-medium mb-6 uppercase">
 The Wedding Of
 </p>
 </div>
 
 <div ref="el => { if(el) textRefs[1] = el }" class="opacity-0 invisible relative">
 <h1 class="text-on-surface text-5xl md:text-8xl lg:text-9xl font-serif mb-4">
 <span class="absolute -top-10 -left-10 text-primary opacity-20 text-8xl md:text-9xl font-serif italic z-[-1]">&</span>
 Romeo <br class="md:hidden"/>
 <span class="text-primary hidden md:inline">&amp;</span> Juliet
 </h1>
 </div>

 <div ref="el => { if(el) textRefs[2] = el }" class="opacity-0 invisible">
 
 </div>

 <div ref="el => { if(el) textRefs[3] = el }" class="opacity-0 invisible">
 <p class="text-on-surface/70 font-sans text-xs md:text-sm tracking-[0.2em] font-light max-w-lg leading-relaxed uppercase mb-4">
 We invite you to celebrate<br/>our special day
 </p>
 </div>

 <div ref="el => { if(el) textRefs[4] = el }" class="opacity-0 invisible">
 <p class="text-on-surface font-sans text-sm md:text-base tracking-[0.1em] font-medium">
 Saturday, Oct 24, 2026
 </p>
 </div>
 </div>
 </section>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import { gsap } from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';

gsap.registerPlugin(ScrollTrigger);

const sectionRef = ref(null);
const bgRef = ref(null);
const ornamentTopLeftRef = ref(null);
const ornamentBottomRightRef = ref(null);
const textRefs = ref([]);
const ctx = ref(null);

onMounted(() => {
 ctx.value = gsap.context(() => {
 const tl = gsap.timeline({
 scrollTrigger: {
 trigger: sectionRef.value,
 start: 'top 80%', // Triggers nicely when entering viewport
 toggleActions: 'play none none none'
 }
 });

 // Step 1: Canvas Scale
 // Slowly scale the background image from 1.1 to 1 over 4 seconds
 tl.fromTo(bgRef.value,
 { scale: 1.1 },
 { scale: 1, duration: 4, ease: 'power1.inOut' },
 0
 );

 // Step 2: The Frame - Floral Ornaments
 // "Grow" into place (scale 0.7, opacity 0, subtle rotation)
 const ornaments = [ornamentTopLeftRef.value, ornamentBottomRightRef.value].filter(Boolean);
 
 tl.fromTo(ornaments,
 { scale: 0.7, autoAlpha: 0, rotation: -8 },
 { 
 scale: 1, 
 autoAlpha: 1, 
 rotation: 0, 
 duration: 2.5, 
 ease: 'power3.out',
 onComplete: () => {
 // Step 3: Floating Loop (Post-Entrance)
 // Add a subtle, infinite "idle" animation (yoyo motion +/- 10px) 
 gsap.to(ornaments, {
 y: 10,
 duration: 3,
 repeat: -1,
 yoyo: true,
 ease: 'sine.inOut'
 });
 }
 },
 0.2 // Starts slightly after the canvas bg scaling
 );

 // Step 3: The Content - Stagger the text reveal
 // Target the Heading, Subheading, and Invitation details.
 // Use y: 50 and autoAlpha: 0 with expo.out ease
 tl.fromTo(textRefs.value,
 { y: 50, autoAlpha: 0 },
 { 
 y: 0, 
 autoAlpha: 1, 
 duration: 1.5, 
 stagger: 0.2, 
 ease: 'expo.out' 
 },
 0.8 // Start after ornaments start appearing
 );

 }, sectionRef.value);
});

onUnmounted(() => {
 // Cleanup GSAP context to avoid memory leaks
 ctx.value?.revert();
});
</script>
