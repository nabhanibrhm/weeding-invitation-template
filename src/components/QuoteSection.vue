<template>
  <section class="py-24 px-6 md:px-12 bg-mulyo-cream text-center overflow-hidden">
    <div 
      ref="quoteContainer"
      class="max-w-4xl mx-auto space-y-8 transition-all duration-1000 transform"
      :class="isVisible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-12'"
    >
      <!-- Decorative Ornament -->
      <div class="flex justify-center mb-6">
        <div class="h-px w-12 bg-mulyo-gold/30 self-center"></div>
        <div class="mx-4 text-mulyo-gold">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1" stroke-linecap="round" stroke-linejoin="round" class="feather feather-heart"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>
        </div>
        <div class="h-px w-12 bg-mulyo-gold/30 self-center"></div>
      </div>

      <!-- The Quote -->
      <blockquote class="relative">
        <span class="absolute -top-10 -left-4 text-8xl text-mulyo-gold/10 font-serif leading-none italic">“</span>
        <p class="text-xl md:text-2xl lg:text-3xl font-playfair italic leading-relaxed text-mulyo-charcoal/80 px-8">
          "And among His signs is that He created for you from yourselves mates that you may find tranquility in them; and He placed between you affection and mercy."
        </p>
        <span class="absolute -bottom-16 -right-4 text-8xl text-mulyo-gold/10 font-serif leading-none italic">”</span>
      </blockquote>

      <!-- Source -->
      <cite class="block text-sm md:text-base font-sans tracking-[0.3em] uppercase text-mulyo-gold pt-4 not-italic">
        — Ar-Rum: 21
      </cite>

      <div class="flex justify-center mt-6">
        <div class="h-px w-24 bg-gradient-to-r from-transparent via-mulyo-gold/20 to-transparent"></div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const isVisible = ref(false);
const quoteContainer = ref(null);

onMounted(() => {
  const observer = new IntersectionObserver((entries) => {
    if (entries[0].isIntersecting) {
      isVisible.value = true;
    }
  }, { threshold: 0.2 });

  if (quoteContainer.value) {
    observer.observe(quoteContainer.value);
  }
});
</script>

<style scoped>
.font-playfair {
  font-family: 'Playfair Display', serif;
}
</style>
