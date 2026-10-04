import { motion } from "framer-motion";
import {
    ArrowUp,
    ChevronDown,
    FileText,
    Folder,
    Menu,
    Plus,
    Search,
    Settings,
    Sparkles,
    Upload,
} from "lucide-react";
import { useState } from "react";
import { researchQuestion } from "../../api/research";

function Chat() {
    const [message, setMessage] = useState("");
    const [sidebarOpen, setSidebarOpen] = useState(true);

    const [messages, setMessages] = useState([]);
    const [loading, setLoading] = useState(false);

    const sendMessage = async () => {
        const question = message.trim();

        if (!question || loading) return;

        setMessages((previous) => [
            ...previous,
            {
                role: "user",
                content: question,
            },
        ]);

        setMessage("");
        setLoading(true);

        try {
            const response = await researchQuestion(question);

            setMessages((previous) => [
                ...previous,
                {
                    role: "assistant",
                    content: response.answer,
                },
            ]);
        } catch (error) {
            setMessages((previous) => [
                ...previous,
                {
                    role: "assistant",
                    content:
                        error.message ||
                        "Something went wrong while contacting Helix.",
                },
            ]);
        } finally {
            setLoading(false);
        }
    };
    return (
        <main className="min-h-screen overflow-hidden bg-[#08090c] text-white">

            {/* Ambient intelligence */}
            <div
                className="
                    pointer-events-none
                    fixed
                    left-1/2
                    top-1/3
                    h-[600px]
                    w-[600px]
                    -translate-x-1/2
                    rounded-full
                    bg-violet-500/[0.025]
                    blur-[160px]
                "
            />

            <div className="relative flex h-screen">

                {/* Sidebar */}
                <motion.aside
                    animate={{
                        width: sidebarOpen ? 270 : 0,
                        opacity: sidebarOpen ? 1 : 0,
                    }}
                    transition={{
                        duration: 0.3,
                        ease: [0.16, 1, 0.3, 1],
                    }}
                    className="
                        relative
                        z-30
                        hidden
                        shrink-0
                        overflow-hidden
                        border-r
                        border-white/[0.07]
                        bg-white/[0.015]
                        backdrop-blur-2xl
                        md:block
                    "
                >
                    <div className="flex h-full w-[270px] flex-col">

                        {/* Brand */}
                        <div className="flex h-20 items-center px-5">

                            <div
                                className="
                                    flex
                                    h-9
                                    w-9
                                    items-center
                                    justify-center
                                    rounded-full
                                    border
                                    border-white/[0.12]
                                    bg-white/[0.05]
                                    shadow-[0_0_35px_rgba(167,139,250,0.05)]
                                "
                            >
                                <span className="text-lg font-medium">
                                    C
                                </span>
                            </div>

                            <div className="ml-3">
                                <p className="text-[11px] font-semibold tracking-[0.22em] text-white/80">
                                    COGNEXA
                                </p>

                                <p className="mt-0.5 text-[8px] uppercase tracking-[0.18em] text-white/20">
                                    Intelligence layer
                                </p>
                            </div>
                        </div>

                        {/* New chat */}
                        <div className="px-4">
                            <button
                                type="button"
                                className="
                                    flex
                                    w-full
                                    items-center
                                    gap-2.5
                                    rounded-xl
                                    border
                                    border-white/[0.08]
                                    bg-white/[0.035]
                                    px-3
                                    py-2.5
                                    text-[10px]
                                    font-medium
                                    text-white/65
                                    transition
                                    hover:bg-white/[0.07]
                                    hover:text-white
                                "
                            >
                                <Plus size={14} />
                                New conversation
                            </button>
                        </div>

                        {/* Navigation */}
                        <div className="mt-7 px-4">

                            <p className="mb-3 px-2 text-[8px] uppercase tracking-[0.25em] text-white/20">
                                Workspace
                            </p>

                            <button
                                type="button"
                                className="
                                    flex
                                    w-full
                                    items-center
                                    gap-3
                                    rounded-xl
                                    bg-white/[0.055]
                                    px-3
                                    py-2.5
                                    text-left
                                    text-[10px]
                                    text-white/70
                                "
                            >
                                <Sparkles size={13} />
                                Intelligence
                            </button>

                            <button
                                type="button"
                                className="
                                    mt-1
                                    flex
                                    w-full
                                    items-center
                                    gap-3
                                    rounded-xl
                                    px-3
                                    py-2.5
                                    text-left
                                    text-[10px]
                                    text-white/35
                                    transition
                                    hover:bg-white/[0.035]
                                    hover:text-white/65
                                "
                            >
                                <Folder size={13} />
                                Projects
                            </button>

                            <button
                                type="button"
                                className="
                                    mt-1
                                    flex
                                    w-full
                                    items-center
                                    gap-3
                                    rounded-xl
                                    px-3
                                    py-2.5
                                    text-left
                                    text-[10px]
                                    text-white/35
                                    transition
                                    hover:bg-white/[0.035]
                                    hover:text-white/65
                                "
                            >
                                <FileText size={13} />
                                Documents
                            </button>
                        </div>

                        {/* Recent */}
                        <div className="mt-8 flex-1 overflow-y-auto px-4">

                            <p className="mb-3 px-2 text-[8px] uppercase tracking-[0.25em] text-white/20">
                                Recent
                            </p>

                            {[
                                "Market intelligence",
                                "Research synthesis",
                                "HAC architecture",
                            ].map((item) => (
                                <button
                                    key={item}
                                    type="button"
                                    className="
                                        block
                                        w-full
                                        truncate
                                        rounded-lg
                                        px-2
                                        py-2
                                        text-left
                                        text-[10px]
                                        text-white/25
                                        transition
                                        hover:bg-white/[0.03]
                                        hover:text-white/55
                                    "
                                >
                                    {item}
                                </button>
                            ))}
                        </div>

                        {/* Bottom */}
                        <div className="border-t border-white/[0.06] p-4">

                            <button
                                type="button"
                                className="
                                    flex
                                    w-full
                                    items-center
                                    gap-3
                                    rounded-xl
                                    px-3
                                    py-2.5
                                    text-[10px]
                                    text-white/30
                                    transition
                                    hover:bg-white/[0.035]
                                    hover:text-white/60
                                "
                            >
                                <Settings size={13} />
                                Settings
                            </button>

                        </div>
                    </div>
                </motion.aside>

                {/* Main */}
                <section className="relative flex min-w-0 flex-1 flex-col">

                    {/* Header */}
                    <header
                        className="
                            flex
                            h-20
                            shrink-0
                            items-center
                            justify-between
                            border-b
                            border-white/[0.06]
                            px-5
                            sm:px-8
                        "
                    >
                        <div className="flex items-center gap-3">

                            <button
                                type="button"
                                onClick={() => setSidebarOpen((value) => !value)}
                                className="
                                    rounded-lg
                                    p-2
                                    text-white/30
                                    transition
                                    hover:bg-white/[0.05]
                                    hover:text-white
                                    md:hidden
                                "
                            >
                                <Menu size={16} />
                            </button>

                            <div>
                                <div className="flex items-center gap-2">
                                    <span className="text-[11px] font-medium text-white/70">
                                        Intelligence
                                    </span>

                                    <ChevronDown
                                        size={12}
                                        className="text-white/20"
                                    />
                                </div>

                                <p className="mt-1 text-[8px] uppercase tracking-[0.22em] text-white/15">
                                    Helix Engine
                                </p>
                            </div>
                        </div>

                        <button
                            type="button"
                            className="
                                flex
                                items-center
                                gap-2
                                rounded-full
                                border
                                border-white/[0.08]
                                bg-white/[0.035]
                                px-3
                                py-2
                                text-[9px]
                                text-white/40
                                transition
                                hover:bg-white/[0.07]
                                hover:text-white/70
                            "
                        >
                            <span className="h-1.5 w-1.5 rounded-full bg-emerald-300/70" />
                            Helix ready
                        </button>
                    </header>

                    {/* Conversation */}
                    <div className="flex-1 overflow-y-auto">
                        <div className="mx-auto flex min-h-full w-full max-w-4xl flex-col px-5 pb-10 pt-16 sm:px-8">

                            {messages.length === 0 ? (
                                /* Empty state */
                                <div className="flex flex-1 flex-col items-center justify-center text-center">

                                    <motion.div
                                        initial={{ opacity: 0, scale: 0.9 }}
                                        animate={{ opacity: 1, scale: 1 }}
                                        transition={{ duration: 0.7 }}
                                        className="
                        relative
                        mb-8
                        flex
                        h-20
                        w-20
                        items-center
                        justify-center
                        rounded-full
                        border
                        border-white/[0.10]
                        bg-white/[0.025]
                        shadow-[0_0_80px_rgba(167,139,250,0.06)]
                    "
                                    >
                                        <span className="absolute inset-2 rounded-full border border-violet-200/[0.08]" />

                                        <span className="text-3xl font-medium tracking-[-0.1em] text-white/90">
                                            C
                                        </span>
                                    </motion.div>

                                    <p className="text-[9px] uppercase tracking-[0.35em] text-violet-200/40">
                                        Cognexa Intelligence
                                    </p>

                                    <h1 className="mt-4 text-3xl font-medium tracking-[-0.04em] text-white/90 sm:text-4xl">
                                        What would you like
                                        <br />
                                        to understand?
                                    </h1>

                                    <p className="mt-5 max-w-md text-sm leading-6 text-white/25">
                                        Ask Cognexa to research, connect, retrieve,
                                        and synthesize information through Helix.
                                    </p>

                                    <div className="mt-10 grid w-full max-w-2xl gap-2 sm:grid-cols-2">

                                        {[
                                            "Research a market opportunity",
                                            "Analyze a document",
                                            "Compare competing companies",
                                            "Build a research brief",
                                        ].map((suggestion) => (
                                            <button
                                                key={suggestion}
                                                type="button"
                                                onClick={() => setMessage(suggestion)}
                                                className="
                                rounded-2xl
                                border
                                border-white/[0.07]
                                bg-white/[0.02]
                                px-4
                                py-3
                                text-left
                                text-[10px]
                                text-white/35
                                transition
                                hover:border-violet-200/[0.15]
                                hover:bg-white/[0.04]
                                hover:text-white/65
                            "
                                            >
                                                {suggestion}
                                            </button>
                                        ))}

                                    </div>
                                </div>
                            ) : (
                                /* Messages */
                                <div className="w-full space-y-6">

                                    {messages.map((item, index) => (
                                        <motion.div
                                            key={index}
                                            initial={{ opacity: 0, y: 8 }}
                                            animate={{ opacity: 1, y: 0 }}
                                            transition={{ duration: 0.25 }}
                                            className={
                                                item.role === "user"
                                                    ? "flex justify-end"
                                                    : "flex justify-start"
                                            }
                                        >
                                            <div
                                                className={
                                                    item.role === "user"
                                                        ? `
                                        max-w-[80%]
                                        rounded-2xl
                                        rounded-br-md
                                        border
                                        border-white/[0.08]
                                        bg-white/[0.06]
                                        px-4
                                        py-3
                                        text-sm
                                        leading-6
                                        text-white/80
                                    `
                                                        : `
                                        max-w-[85%]
                                        rounded-2xl
                                        rounded-bl-md
                                        border
                                        border-violet-200/[0.08]
                                        bg-violet-200/[0.025]
                                        px-5
                                        py-4
                                        text-sm
                                        leading-7
                                        text-white/70
                                    `
                                                }
                                            >
                                                {item.role === "assistant" && (
                                                    <div className="mb-2 flex items-center gap-2">
                                                        <span className="flex h-5 w-5 items-center justify-center rounded-full border border-white/[0.10] bg-white/[0.04] text-[9px] text-white/70">
                                                            C
                                                        </span>

                                                        <span className="text-[8px] uppercase tracking-[0.2em] text-violet-200/40">
                                                            Helix
                                                        </span>
                                                    </div>
                                                )}

                                                <p className="whitespace-pre-wrap">
                                                    {item.content}
                                                </p>
                                            </div>
                                        </motion.div>
                                    ))}

                                    {/* Loading */}
                                    {loading && (
                                        <motion.div
                                            initial={{ opacity: 0, y: 8 }}
                                            animate={{ opacity: 1, y: 0 }}
                                            className="flex justify-start"
                                        >
                                            <div
                                                className="
                                rounded-2xl
                                rounded-bl-md
                                border
                                border-violet-200/[0.08]
                                bg-violet-200/[0.025]
                                px-5
                                py-4
                            "
                                            >
                                                <div className="flex items-center gap-3">

                                                    <div className="flex h-5 w-5 items-center justify-center rounded-full border border-white/[0.10] bg-white/[0.04]">
                                                        <motion.div
                                                            animate={{
                                                                rotate: 360,
                                                            }}
                                                            transition={{
                                                                duration: 1.2,
                                                                repeat: Infinity,
                                                                ease: "linear",
                                                            }}
                                                            className="
                                            h-2.5
                                            w-2.5
                                            rounded-full
                                            border
                                            border-white/20
                                            border-t-violet-200/80
                                        "
                                                        />
                                                    </div>

                                                    <div>
                                                        <p className="text-[10px] text-white/50">
                                                            Helix is thinking...
                                                        </p>

                                                        <p className="mt-1 text-[8px] uppercase tracking-[0.18em] text-white/20">
                                                            Retrieving · Reasoning · Synthesizing
                                                        </p>
                                                    </div>

                                                </div>
                                            </div>
                                        </motion.div>
                                    )}

                                </div>
                            )}

                        </div>
                    </div>
                    {/* Composer */}
                    <div className="shrink-0 px-5 pb-5 sm:px-8 sm:pb-7">

                        <div className="mx-auto max-w-4xl">

                            <div
                                className="
                                    relative
                                    rounded-[24px]
                                    border
                                    border-white/[0.09]
                                    bg-white/[0.035]
                                    shadow-[inset_0_1px_1px_rgba(255,255,255,0.06),0_20px_80px_rgba(0,0,0,0.22)]
                                    backdrop-blur-2xl
                                "
                            >

                                {/* Top reflection */}
                                <span
                                    className="
                                        pointer-events-none
                                        absolute
                                        inset-x-[12%]
                                        top-0
                                        h-px
                                        bg-gradient-to-r
                                        from-transparent
                                        via-white/20
                                        to-transparent
                                    "
                                />

                                <textarea
                                    value={message}
                                    onChange={(event) => setMessage(event.target.value)}
                                    onKeyDown={(event) => {
                                        if (
                                            event.key === "Enter" &&
                                            !event.shiftKey
                                        ) {
                                            event.preventDefault();
                                            sendMessage();
                                        }
                                    }}
                                    rows={2}
                                    placeholder="Ask Cognexa anything..."
                                    className="
                                        w-full
                                        resize-none
                                        bg-transparent
                                        px-5
                                        pb-14
                                        pt-5
                                        text-sm
                                        leading-6
                                        text-white/80
                                        outline-none
                                        placeholder:text-white/20
                                    "
                                />

                                <div className="absolute bottom-3 left-3 right-3 flex items-center justify-between">

                                    <div className="flex items-center gap-1">

                                        <button
                                            type="button"
                                            className="
                                                rounded-xl
                                                p-2
                                                text-white/25
                                                transition
                                                hover:bg-white/[0.06]
                                                hover:text-white/60
                                            "
                                        >
                                            <Upload size={14} />
                                        </button>

                                        <button
                                            type="button"
                                            className="
                                                rounded-xl
                                                p-2
                                                text-white/25
                                                transition
                                                hover:bg-white/[0.06]
                                                hover:text-white/60
                                            "
                                        >
                                            <Search size={14} />
                                        </button>

                                    </div>

                                    <button
                                        type="button"
                                        onClick={sendMessage}
                                        className="
                                            flex
                                            h-8
                                            w-8
                                            items-center
                                            justify-center
                                            rounded-full
                                            bg-white
                                            text-black
                                            transition
                                            hover:bg-white/90
                                        "
                                    >
                                        <ArrowUp size={14} />
                                    </button>

                                </div>
                            </div>

                            <p className="mt-3 text-center text-[8px] tracking-[0.08em] text-white/10">
                                Cognexa can make mistakes. Verify important information.
                            </p>

                        </div>
                    </div>

                </section>
            </div>
        </main>
    );
}

export default Chat;

