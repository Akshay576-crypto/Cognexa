import { motion } from "framer-motion";

const blocks = [
    {
        type: "heading",
        text: "1. Introduction",
    },
    {
        type: "paragraph",
        text: "Cognexa transforms complex information into structured knowledge.",
    },
    {
        type: "paragraph",
        text: "Understanding document structure is essential before semantic retrieval.",
    },
    {
        type: "heading",
        text: "2. Methodology",
    },
    {
        type: "table",
        text: "Research Data        Results",
    },
    {
        type: "paragraph",
        text: "The system preserves relationships between meaningful sections.",
    },
];

function HACDocument() {
    return (
        <motion.div
            initial={{ opacity: 0, y: 30, scale: 0.97 }}
            whileInView={{ opacity: 1, y: 0, scale: 1 }}
            viewport={{ once: true, amount: 0.3 }}
            transition={{
                duration: 0.9,
                ease: [0.16, 1, 0.3, 1],
            }}
            className="
                relative
                w-full
                max-w-[560px]
                overflow-hidden
                rounded-[30px]
                border
                border-white/[0.10]
                bg-white/[0.035]
                p-6
                shadow-[inset_0_1px_1px_rgba(255,255,255,0.10),0_30px_90px_rgba(0,0,0,0.25)]
                backdrop-blur-[30px]
            "
        >
            {/* Glass reflection */}
            <div
                className="
                    pointer-events-none
                    absolute
                    inset-x-10
                    top-0
                    h-px
                    bg-gradient-to-r
                    from-transparent
                    via-white/30
                    to-transparent
                "
            />

            {/* Document header */}
            <div className="relative z-10 mb-6 flex items-center justify-between">
                <div>
                    <p className="text-[8px] uppercase tracking-[0.28em] text-white/25">
                        Source document
                    </p>

                    <h3 className="mt-1 text-sm font-medium text-white/80">
                        Research Report.pdf
                    </h3>
                </div>

                <div className="flex items-center gap-2 rounded-full border border-violet-300/[0.12] bg-violet-300/[0.04] px-3 py-1.5">
                    <span className="h-1.5 w-1.5 animate-pulse rounded-full bg-violet-300 shadow-[0_0_12px_rgba(196,181,253,0.8)]" />

                    <span className="text-[8px] uppercase tracking-[0.2em] text-violet-200/60">
                        Structure detected
                    </span>
                </div>
            </div>

            {/* Document content */}
            <div className="relative z-10 space-y-4">
                {blocks.map((block, index) => (
                    <motion.div
                        key={index}
                        initial={{ opacity: 0, x: -10 }}
                        whileInView={{ opacity: 1, x: 0 }}
                        viewport={{ once: true }}
                        transition={{
                            duration: 0.5,
                            delay: index * 0.08,
                        }}
                    >
                        {block.type === "heading" && (
                            <div className="flex items-center gap-3">
                                <span className="h-1.5 w-1.5 rounded-full bg-violet-300/70 shadow-[0_0_10px_rgba(196,181,253,0.5)]" />

                                <span className="text-[10px] font-medium tracking-wide text-white/65">
                                    {block.text}
                                </span>
                            </div>
                        )}

                        {block.type === "paragraph" && (
                            <div className="ml-4 rounded-xl border border-white/[0.045] bg-white/[0.018] px-4 py-3">
                                <p className="text-[10px] leading-5 text-white/30">
                                    {block.text}
                                </p>
                            </div>
                        )}

                        {block.type === "table" && (
                            <div className="ml-4 overflow-hidden rounded-xl border border-white/[0.06]">
                                <div className="grid grid-cols-2 bg-white/[0.035] px-4 py-3">
                                    {block.text.split("        ").map((item) => (
                                        <span
                                            key={item}
                                            className="text-[9px] uppercase tracking-[0.12em] text-white/35"
                                        >
                                            {item}
                                        </span>
                                    ))}
                                </div>
                            </div>
                        )}
                    </motion.div>
                ))}
            </div>

            {/* Footer */}
            <div className="relative z-10 mt-6 flex items-center justify-between border-t border-white/[0.06] pt-4">
                <span className="text-[8px] uppercase tracking-[0.2em] text-white/20">
                    Raw information
                </span>

                <span className="text-[8px] uppercase tracking-[0.2em] text-white/15">
                    Awaiting HAC
                </span>
            </div>
        </motion.div>
    );
}

export default HACDocument;