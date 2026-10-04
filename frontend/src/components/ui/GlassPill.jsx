function GlassPill({ children, className = "" }) {
    return (
        <div
            className={`
        inline-flex
        items-center
        gap-2
        rounded-full
        border
        border-white/[0.12]
        bg-white/[0.045]
        px-4
        py-2
        text-[10px]
        uppercase
        tracking-[0.22em]
        text-white/55
        shadow-[inset_0_1px_0_rgba(255,255,255,0.12)]
        backdrop-blur-2xl
        ${className}
      `}
        >
            <span className="h-1.5 w-1.5 rounded-full bg-violet-300 shadow-[0_0_12px_rgba(196,181,253,0.8)]" />

            {children}
        </div>
    );
}

export default GlassPill;