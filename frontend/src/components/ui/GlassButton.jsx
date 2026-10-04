import { ArrowUpRight } from "lucide-react";

function GlassButton({
    children,
    variant = "glass",
    icon = true,
}) {
    const variants = {
        glass: `
      border-white/[0.14]
      bg-white/[0.07]
      text-white
      hover:bg-white/[0.12]
    `,
        bright: `
      border-white/50
      bg-white/90
      text-black
      hover:bg-white
    `,
    };

    return (
        <button
            className={`
        group
        relative
        flex
        items-center
        gap-3
        overflow-hidden
        rounded-full
        border
        px-6
        py-3.5
        text-sm
        font-medium
        backdrop-blur-2xl
        transition-all
        duration-300
        hover:-translate-y-0.5
        ${variants[variant]}
      `}
        >
            {/* moving reflection */}
            <span
                className="
          pointer-events-none
          absolute
          inset-y-0
          -left-20
          w-16
          rotate-12
          bg-white/20
          blur-xl
          transition-all
          duration-700
          group-hover:left-[120%]
        "
            />

            <span className="relative z-10">
                {children}
            </span>

            {icon && (
                <ArrowUpRight
                    size={16}
                    className="
            relative
            z-10
            transition-transform
            duration-300
            group-hover:translate-x-0.5
            group-hover:-translate-y-0.5
          "
                />
            )}
        </button>
    );
}

export default GlassButton;