function GlassSurface({
    children,
    className = "",
    intensity = "normal",
}) {
    const intensityClasses = {
        subtle: "bg-white/[0.025]",
        normal: "bg-white/[0.055]",
        strong: "bg-white/[0.085]",
    };

    return (
        <div
            className={`
        relative
        overflow-hidden
        rounded-[28px]
        border
        border-white/[0.13]
        ${intensityClasses[intensity]}
        backdrop-blur-[28px]
        backdrop-saturate-150
        shadow-[inset_0_1px_0_rgba(255,255,255,0.16),0_20px_80px_rgba(0,0,0,0.18)]
        ${className}
      `}
        >
            {/* Liquid reflection */}
            <div
                className="
          pointer-events-none
          absolute
          inset-x-0
          top-0
          h-px
          bg-gradient-to-r
          from-transparent
          via-white/35
          to-transparent
        "
            />

            {/* Soft internal light */}
            <div
                className="
          pointer-events-none
          absolute
          -right-20
          -top-20
          h-40
          w-40
          rounded-full
          bg-white/[0.06]
          blur-3xl
        "
            />

            <div className="relative z-10">
                {children}
            </div>
        </div>
    );
}

export default GlassSurface;