<template>
 <div class="fixed inset-0 pointer-events-none z-0 overflow-hidden floating-container">
 <div
 v-for="n in 25"
 :key="n"
 class="particle absolute rounded-full bg-gradient-to-br from-primary via-primary/70 to-transparent backdrop-blur-sm "
 style="clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);"
 ></div>
 </div>
</template>

<script setup>
import { onMounted, onUnmounted } from 'vue';
import gsap from 'gsap';

let timelines = [];

onMounted(() => {
 const particles = document.querySelectorAll('.particle');
 
 particles.forEach((p) => {
 // Initial random distribution
 gsap.set(p, {
 x: `random(0, ${window.innerWidth})`,
 y: `random(0, ${window.innerHeight})`,
 scale: "random(0.3, 1)",
 rotation: "random(0, 360)",
 opacity: "random(0.15, 0.6)",
 width: "random(6, 14)px",
 height: "random(6, 14)px"
 });

 const speed = Math.random() * 20 + 20;

 // Upward drift timeline (Continuous loop from bottom to top)
 const driftTl = gsap.timeline({ repeat: -1 });
 
 // First animation: from current random Y to the top
 const currentY = gsap.getProperty(p, "y");
 const distanceRatio = (currentY + 100) / (window.innerHeight + 100);
 
 driftTl.to(p, {
 y: -100,
 duration: speed * distanceRatio,
 ease: "none"
 })
 .set(p, {
 y: window.innerHeight + 100,
 x: () => Math.random() * window.innerWidth // New X on respawn
 })
 .to(p, {
 y: -100,
 duration: speed,
 ease: "none"
 });

 // Independent swaying and rotation
 const swayTl = gsap.to(p, {
 x: "+=random(-60, 60)",
 rotation: "+=random(-180, 180)",
 duration: "random(5, 10)",
 ease: "sine.inOut",
 repeat: -1,
 yoyo: true
 });

 timelines.push(driftTl, swayTl);
 });
});

onUnmounted(() => {
 // Clean up GSAP timelines
 timelines.forEach(tl => tl.kill());
});
</script>

<style scoped>
.floating-container {
 /* Ensure it doesn't block any clicks */
 pointer-events: none;
}
</style>
