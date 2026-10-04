import { motion } from "framer-motion";

function HeroBackground() {
    return (
        <div className="pointer-events-none absolute inset-0 overflow-hidden">

            {/* Deep graphite environment */}
            <div className="absolute inset-0 bg-[#08090c]" />

            {/* Soft pearl atmosphere */}
            <motion.div
                animate={{
                    x: ["-5%", "5%", "-5%"],
                    y: ["-4%", "5%", "-4%"],
                    scale: [1, 1.12, 1],
                    opacity: [0.16, 0.24, 0.16],
                }}
                transition={{
                    duration: 20,
                    repeat: Infinity,
                    ease: "easeInOut",
                }}
                className="
                    absolute
                    left-[-12%]
                    top-[12%]
                    h-[700px]
                    w-[700px]
                    rounded-full
                    bg-white/[0.035]
                    blur-[180px]
                "
            />

            {/* Extremely subtle lavender refraction */}
            <motion.div
                animate={{
                    x: ["4%", "-4%", "4%"],
                    y: ["-3%", "5%", "-3%"],
                    scale: [1, 1.1, 1],
                    opacity: [0.08, 0.14, 0.08],
                }}
                transition={{
                    duration: 24,
                    repeat: Infinity,
                    ease: "easeInOut",
                }}
                className="
                    absolute
                    right-[-15%]
                    top-[18%]
                    h-[620px]
                    w-[620px]
                    rounded-full
                    bg-[#c8bfff]/[0.055]
                    blur-[190px]
                "
            />

            {/* Central liquid-glass illumination */}
            <motion.div
                animate={{
                    scale: [0.9, 1.12, 0.9],
                    opacity: [0.08, 0.17, 0.08],
                }}
                transition={{
                    duration: 12,
                    repeat: Infinity,
                    ease: "easeInOut",
                }}
                className="
                    absolute
                    left-1/2
                    top-[45%]
                    h-[720px]
                    w-[720px]
                    -translate-x-1/2
                    -translate-y-1/2
                    rounded-full
                    bg-white/[0.025]
                    blur-[150px]
                "
            />

            {/* Tiny ambient reflections */}
            <motion.div
                animate={{ opacity: [0.15, 0.4, 0.15] }}
                transition={{
                    duration: 5,
                    repeat: Infinity,
                }}
                className="
                    absolute
                    left-[18%]
                    top-[30%]
                    h-1.5
                    w-1.5
                    rounded-full
                    bg-white/30
                    blur-[1px]
                "
            />

            <motion.div
                animate={{ opacity: [0.1, 0.3, 0.1] }}
                transition={{
                    duration: 7,
                    repeat: Infinity,
                }}
                className="
                    absolute
                    right-[20%]
                    top-[25%]
                    h-1
                    w-1
                    rounded-full
                    bg-[#d9dce3]/30
                "
            />

            {/* Spatial vignette */}
            <div
                className="
                    absolute
                    inset-0
                    bg-[radial-gradient(circle_at_center,transparent_15%,rgba(8,9,12,0.82)_100%)]
                "
            />

            {/* Bottom fade */}
            <div
                className="
                    absolute
                    inset-x-0
                    bottom-0
                    h-56
                    bg-gradient-to-t
                    from-[#08090c]
                    to-transparent
                "
            />
        </div>
    );
}

export default HeroBackground;