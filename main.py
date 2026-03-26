#!/usr/bin/env python3
"""
AI辅助短视频脚本生成器 - 主程序
模拟基于大模型的短视频脚本生成功能
"""

import json
import random
import datetime
from typing import Dict, List, Optional


class AIScriptGenerator:
    """AI脚本生成器核心类"""
    
    def __init__(self):
        """初始化生成器，加载预设模板和知识库"""
        self.script_templates = {
            "科普类": self._generate_science_template,
            "教育类": self._generate_education_template,
            "生活技巧类": self._generate_lifehack_template,
            "科技解读类": self._generate_tech_template
        }
        
        # 模拟知识库数据
        self.knowledge_base = {
            "热门话题": ["人工智能发展", "气候变化", "健康养生", "编程学习", "心理学常识"],
            "常用结构": ["问题-解决方案", "现象-原理-应用", "故事-启示", "对比分析", "步骤教学"]
        }
    
    def _generate_science_template(self, topic: str) -> Dict:
        """生成科普类脚本模板"""
        return {
            "标题": f"科普：{topic}的奥秘",
            "时长": "60秒",
            "结构": [
                {"时长": "10s", "内容": f"开头提问：你知道{topic}吗？"},
                {"时长": "20s", "内容": "核心原理讲解（简单易懂）"},
                {"时长": "15s", "内容": "实际应用场景展示"},
                {"时长": "10s", "内容": "总结与思考题"},
                {"时长": "5s", "内容": "结尾互动：评论区分享你的看法"}
            ],
            "标签": ["科普", "知识", topic, "学习"]
        }
    
    def _generate_education_template(self, topic: str) -> Dict:
        """生成教育类脚本模板"""
        return {
            "标题": f"快速掌握：{topic}入门指南",
            "时长": "90秒",
            "结构": [
                {"时长": "15s", "内容": "学习目标介绍"},
                {"时长": "30s", "内容": "核心概念讲解"},
                {"时长": "25s", "内容": "实操演示"},
                {"时长": "15s", "内容": "常见错误提醒"},
                {"时长": "5s", "内容": "课后练习建议"}
            ],
            "标签": ["教育", "教程", "学习", topic]
        }
    
    def _generate_lifehack_template(self, topic: str) -> Dict:
        """生成生活技巧类脚本模板"""
        return {
            "标题": f"实用技巧：{topic}的小妙招",
            "时长": "45秒",
            "结构": [
                {"时长": "5s", "内容": "痛点引入"},
                {"时长": "20s", "内容": "技巧演示"},
                {"时长": "15s", "内容": "使用场景展示"},
                {"时长": "5s", "内容": "效果对比"}
            ],
            "标签": ["生活", "技巧", "实用", topic]
        }
    
    def _generate_tech_template(self, topic: str) -> Dict:
        """生成科技解读类脚本模板"""
        return {
            "标题": f"深度解读：{topic}技术前沿",
            "时长": "75秒",
            "结构": [
                {"时长": "10s", "内容": "技术背景介绍"},
                {"时长": "25s", "内容": "核心技术解析"},
                {"时长": "20s", "内容": "行业影响分析"},
                {"时长": "15s", "内容": "未来展望"},
                {"时长": "5s", "内容": "互动提问"}
            ],
            "标签": ["科技", "解读", "前沿", topic]
        }
    
    def generate_script_ideas(self, category: Optional[str] = None) -> List[str]:
        """生成脚本选题建议"""
        if category and category in self.knowledge_base["热门话题"]:
            topics = [category]
        else:
            topics = random.sample(self.knowledge_base["热门话题"], 3)
        
        structures = random.sample(self.knowledge_base["常用结构"], 2)
        
        ideas = []
        for topic in topics:
            for structure in structures:
                ideas.append(f"{topic} - 采用{structure}结构")
        
        return ideas
    
    def generate_script(self, topic: str, category: str) -> Dict:
        """生成完整脚本草稿"""
        if category not in self.script_templates:
            category = random.choice(list(self.script_templates.keys()))
        
        # 调用对应模板生成函数
        script = self.script_templates[category](topic)
        
        # 添加元数据
        script["生成时间"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        script["主题"] = topic
        script["类型"] = category
        script["建议拍摄设备"] = ["手机", "三脚架", "补光灯"]
        script["背景音乐建议"] = "轻快的纯音乐或与主题相关的音效"
        
        return script
    
    def save_script(self, script: Dict, filename: str = None) -> str:
        """保存脚本到JSON文件"""
        if not filename:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"script_{timestamp}.json"
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(script, f, ensure_ascii=False, indent=2)
        
        return filename


def main():
    """主函数 - 程序入口"""
    print("=" * 50)
    print("AI辅助短视频脚本生成器")
    print("=" * 50)
    
    # 初始化生成器
    generator = AIScriptGenerator()
    
    # 用户输入
    print("\n请选择脚本类型：")
    categories = list(generator.script_templates.keys())
    for i, cat in enumerate(categories, 1):
        print(f"{i}. {cat}")
    
    try:
        choice = int(input("\n请输入编号 (1-4): ")) - 1
        if 0 <= choice < len(categories):
            selected_category = categories[choice]
        else:
            selected_category = random.choice(categories)
            print(f"输入无效，已随机选择: {selected_category}")
    except:
        selected_category = random.choice(categories)
        print(f"输入无效，已随机选择: {selected_category}")
    
    # 生成选题建议
    print(f"\n正在为【{selected_category}】生成选题建议...")
    ideas = generator.generate_script_ideas()
    
    print("\n推荐选题：")
    for i, idea in enumerate(ideas[:3], 1):
        print(f"{i}. {idea}")
    
    # 用户选择或输入主题
    topic_input = input("\n请输入主题（直接输入）或选择编号 (1-3): ")
    
    if topic_input.isdigit() and 1 <= int(topic_input) <= 3:
        topic = ideas[int(topic_input)-1].split(" - ")[0]
    else:
        topic = topic_input if topic_input.strip() else random.choice(generator.knowledge_base["热门话题"])
    
    print(f"\n正在生成脚本：【{topic}】- {selected_category}")
    
    # 生成脚本
    script = generator.generate_script(topic, selected_category)
    
    # 显示结果
    print("\n" + "=" * 50)
    print(f"脚本生成完成！")
    print(f"标题: {script['标题']}")
    print(f"时长: {script['时长']}")
    print(f"类型: {script['类型']}")
    
    print("\n脚本结构：")
    for i, section in enumerate(script["结构"], 1):
        print(f"  {i}. [{section['时长']}] {section['内容']}")
    
    print(f"\n标签: {', '.join(script['标签'])}")
    print(f"生成时间: {script['生成时间']}")
    
    # 保存脚本
    save_choice = input("\n是否保存脚本？(y/n): ").lower()
    if save_choice == 'y':
        filename = generator.save_script(script)
        print(f"脚本已保存到: {filename}")
    
    print("\n感谢使用AI辅助短视频脚本生成器！")


if __name__ == "__main__":
    main()