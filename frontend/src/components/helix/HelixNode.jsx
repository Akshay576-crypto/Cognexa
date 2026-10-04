import { motion } from "framer-motion";

function HelixNode({
    label,
    position,
    active = false,
    color = "violet",
}) {
    const colors = {
        violet:
            "border-violet-300/40 bg-violet-300/10 shadow-[0_0_30px_rgba(167,139,250,0.25)]",
        cyan:
            "border-cyan-300/40 bg-cyan-300/10 shadow-[0_0_30px_rgba(103,232,249,0.25)]",
        white:
            "border-white/30 bg-white/10 shadow-[0_0_30px_rgba(255,255,255,0.15)]",
    };

    return (
        <motion.div
            className="absolute"
            style={position}
            animate={{
                y: [0, -5, 0],
            }}
            transition={{
                duration: 4,
                repeat: Infinity,
                ease: "easeInOut",
            }}
        >
            <motion.div
                whileHover={{
                    scale: 1.08,
                }}
                className={`
          group
          relative
          flex
          h-12
          min-w-12
          cursor-pointer
          items-center
          justify-center
          rounded-full
          border
          ${colors[color]}
          backdrop-blur-xl
          transition-all
        `}
            >
                <span
                    className={`
            h-2
            w-2
            rounded-full
            ${active ? "bg-white" : "bg-white/50"}
          `}
                />

                {/* tooltip */}
                <div
                    className="
            pointer-events-none
            absolute
            left-1/2
            top-full
            mt-3
            -translate-x-1/2
            whitespace-nowrap
            rounded-full
            border
            border-white/[0.10]
            bg-black/40
            px-3
            py-1.5
            text-[9px]
            uppercase
            tracking-[0.18em]
            text-white/55
            opacity-0
            backdrop-blur-xl
            transition-opacity
            group-hover:opacity-100
          "
                >
                    {label}
                </div>
            </motion.div>
        </motion.div>
    );
}

export default HelixNode;