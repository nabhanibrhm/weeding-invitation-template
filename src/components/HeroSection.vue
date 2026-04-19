<template>
  <div class="relative h-[100vh] flex flex-col items-center justify-center transform-style-preserve-3d parallax-layer">
    <!-- Parallax background scaled up to compensate for depth -->
    <div class="absolute inset-0 parallax-bg -m-[20px] md:-m-[50px]">
       <div class="w-full h-full bg-[url('@/assets/hero_bg.png')] bg-cover bg-center animate-float opacity-30 mix-blend-multiply"></div>
       <div class="absolute inset-0 bg-gradient-to-t from-mulyo-cream via-transparent to-transparent"></div>
    </div>
    
    <!-- Parallax foreground text -->
    <div class="relative z-10 flex flex-col items-center justify-center text-center px-4 parallax-fg pt-20">
       <p class="text-mulyo-gold tracking-[0.4em] text-xs md:text-sm font-sans font-medium mb-8 uppercase animate-fade-in opacity-0" style="animation-delay: 0.5s;">The Wedding Of</p>
       <h1 class="text-mulyo-charcoal text-5xl md:text-8xl lg:text-9xl font-playfair mb-6 animate-slide-up opacity-0 relative" style="animation-delay: 0.8s;">
         <span class="absolute -top-10 -left-10 text-mulyo-gold opacity-20 text-8xl md:text-9xl font-serif italic z-[-1]">&</span>
         Romeo <br class="md:hidden"/>
         <span class="text-mulyo-gold hidden md:inline">&amp;</span> Juliet
       </h1>
       <div class="w-[1px] h-16 bg-mulyo-gold mt-8 mb-6 mx-auto animate-slide-up opacity-0 origin-top" style="animation-delay: 1.2s; transform-origin: top; animation-name: growLine;"></div>
       <p class="text-mulyo-charcoal/70 font-sans text-xs md:text-sm tracking-[0.2em] font-light max-w-lg mt-4 animate-fade-in opacity-0 leading-relaxed uppercase" style="animation-delay: 1.5s;">
         We invite you to celebrate<br/>our special day
       </p>
       <p class="text-mulyo-charcoal font-sans text-sm md:text-base tracking-[0.1em] font-medium mt-6 animate-fade-in opacity-0" style="animation-delay: 1.7s;">
         Saturday, Oct 24, 2026
       </p>
    </div>
  </div>
</template>

<style scoped>
.transform-style-preserve-3d {
  transform-style: preserve-3d;
}

@keyframes growLine {
  0% { transform: scaleY(0); opacity: 0; }
  100% { transform: scaleY(1); opacity: 1; }
}

/* Ensure the hero section doesn't collapse */
.parallax-layer {
  min-height: 100vh;
}
</style>
