import { motion } from "framer-motion";
import { ArrowDown } from "lucide-react";

import SemanticSpace from "./SemanticSpace";
import EmbeddingFlow from "./EmbeddingFlow";

function EmbeddingsSection() {
    return (
        <section
            id="embeddings"
            className="
                relative
                min-h-screen
                overflow-hidden
                bg-[#08090c]
                px-6
                py-32
                lg:px-10
                lg:py-44
            "
        >
            {/* Ambient atmosphere */}
            <div
                className="
                    pointer-events-none
                    absolute
                    left-1/2
                    top-[35%]
                    h-[600px]
                    w-[600px]
                    -translate-x-1/2
                    -translate-y-1/2
                    rounded-full
                    bg-cyan-400/[0.025]
                    blur-[150px]
                "
            />

            <div className="relative z-10 mx-auto max-w-[1250px]">

                {/* Heading */}
                <motion.div
                    initial={{ opacity: 0, y: 25 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true, amount: 0.3 }}
                    transition={{
                        duration: 0.8,
                        ease: [0.16, 1, 0.3, 1],
                    }}
                    className="max-w-3xl"
                >
                    <p className="
                        mb-5
                        text-[10px]
                        font-medium
                        uppercase
                        tracking-[0.3em]
                        text-cyan-300/60
                    ">
                        Embeddings
                    </p>

                    <h2 className="
                        text-4xl
                        font-medium
                        leading-[1.02]
                        tracking-[-0.055em]
                        text-white
                        sm:text-5xl
                        lg:text-7xl
                    ">
                        Information becomes
                        <br />
                        <span className="text-white/30">
                            meaning.
                        </span>
                    </h2>

                    <p className="
                        mt-7
                        max-w-2xl
                        text-sm
                        leading-7
                        text-white/40
                        sm:text-base
                    ">
                        Cognexa transforms structured information into
                        semantic representations, allowing systems to
                        understand relationships rather than simply
                        matching words.
                    </p>
                </motion.div>

                {/* Embedding pipeline */}
                <motion.div
                    initial={{ opacity: 0, y: 30 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true, amount: 0.2 }}
                    transition={{
                        duration: 0.8,
                        delay: 0.15,
                    }}
                    className="mt-20"
                >
                    <EmbeddingFlow />
                </motion.div>

                {/* Semantic space */}
                <motion.div
                    initial={{ opacity: 0, y: 35 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true, amount: 0.2 }}
                    transition={{
                        duration: 0.9,
                        delay: 0.25,
                    }}
                    className="mt-5"
                >
                    <SemanticSpace />
                </motion.div>

                {/* Explanation */}
                <div className="
                    mt-16
                    grid
                    gap-8
                    border-t
                    border-white/[0.06]
                    pt-10
                    md:grid-cols-3
                ">
                    <div>
                        <span className="
                            text-[8px]
                            uppercase
                            tracking-[0.25em]
                            text-white/20
                        ">
                            01
                        </span>

                        <h3 className="mt-3 text-sm font-medium text-white/70">
                            Preserve context
                        </h3>

                        <p className="
                            mt-2
                            text-xs
                            leading-6
                            text-white/30
                        ">
                            HAC first preserves the structure and context
                            of the original information.
                        </p>
                    </div>

                    <div>
                        <span className="
                            text-[8px]
                            uppercase
                            tracking-[0.25em]
                            text-white/20
                        ">
                            02
                        </span>

                        <h3 className="mt-3 text-sm font-medium text-white/70">
                            Encode meaning
                        </h3>

                        <p className="
                            mt-2
                            text-xs
                            leading-6
                            text-white/30
                        ">
                            The resulting knowledge is represented in a
                            semantic vector space.
                        </p>
                    </div>

                    <div>
                        <span className="
                            text-[8px]
                            uppercase
                            tracking-[0.25em]
                            text-white/20
                        ">
                            03
                        </span>

                        <h3 className="mt-3 text-sm font-medium text-white/70">
                            Discover relationships
                        </h3>

                        <p className="
                            mt-2
                            text-xs
                            leading-6
                            text-white/30
                        ">
                            Similar meanings become mathematically closer,
                            preparing the knowledge for intelligent retrieval.
                        </p>
                    </div>
                </div>

                {/* Transition */}
                <motion.div
                    initial={{ opacity: 0 }}
                    whileInView={{ opacity: 1 }}
                    viewport={{ once: true }}
                    transition={{ duration: 1 }}
                    className="
                        mt-20
                        flex
                        flex-col
                        items-center
                        gap-3
                        text-center
                    "
                >
                    <span className="
                        text-[9px]
                        uppercase
                        tracking-[0.3em]
                        text-white/15
                    ">
                        From meaning to retrieval
                    </span>

                    <ArrowDown
                        size={14}
                        className="text-cyan-300/40"
                    />
                </motion.div>

            </div>
        </section>
    );
}

export default EmbeddingsSection;